from datetime import date, timedelta
import os, sys, requests, json

if os.name == 'nt':
    sys.path.append("C:\\Users\\brian\\Documents\\Python\\OIC_Web_Apps\\")
else:
    sys.path.append("/home/OIC/OIC_Web_Apps/") # Uncomment on production server
    # sys.path.append("/home/BrianC68/oicdev/OIC_Web_Apps/") # Uncomment on development server
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OIC_Web_Apps.settings')

import django
django.setup()

from django.db import IntegrityError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from kranich.models import KranichSkateDate, KranichSkateSession
from accounts.models import Profile

User = get_user_model()

skate_dates = []


def get_schedule_data(from_date, to_date):
    '''Request schedule data from Schedule Werks for the specified period.'''
    
    url = f"https://ozaukeeicecenter.schedulewerks.com/public/ajax/swCalGet?tid=-1&from={from_date}&to={to_date}&Complex=-1"

    try:
        response = requests.get(url)
        data = json.loads(response.text)
    except requests.exceptions.RequestException as e:
        # print(e)
        return

    for item in data:
        if "Kranich" in item["text"]:
            skate_date = item["start_date"].split(" ")[0]
            skate_date = f"{skate_date[6:]}-{skate_date[:2]}-{skate_date[3:5]}"
            start_time = item["st"].replace("P", "").replace("A", "")
            end_time = item["et"].replace("P", "").replace("A", "")

            skate_dates.append([skate_date, start_time, end_time])
    return

def add_skate_dates(sessions):
    '''Adds Kranich Skate dates and times to the KranichSkateDate model.'''
    model = KranichSkateDate
    new_dates = False

    for session in sessions:
        try:
            data = model(skate_date=session[0], start_time=session[1], end_time=session[2])
            data.save()
            new_dates = True
        except IntegrityError:
            continue
    # print(new_dates)
    return new_dates

def add_john_to_skate():
    '''Adds John Kranich to skate.'''
    skate_dates = KranichSkateDate.objects.filter(skate_date__gt=date.today())
    user = User.objects.get(pk=870)
    print(user)

    for skate_date in skate_dates:
        try:
            KranichSkateSession(skater=user, skate_date=skate_date, paid=True).save()
        except IntegrityError:
            pass

def send_skate_dates_email():
    '''Sends email to Users letting them know when Kranich Skate dates are added.'''
    recipients = Profile.objects.filter(kranich_email=True).select_related('user')

    for recipient in recipients:
        if recipient.user.is_active:
            to_email = [recipient.user.email]
            from_email = 'no-reply@mg.oicwebapps.com'
            subject = 'New Kranich Skate Date Added'

            # Build the plain text message
            text_message = f'Hi {recipient.user.first_name},\n\n'
            text_message += f'New Kranich Skate dates are now available online. Sign up at the url below.\n\n'
            text_message += f'https://www.oicwebapps.com/web_apps/kranich/\n\n'
            text_message += f'If you no longer wish to receive these emails, log in to your account,\n'
            text_message += f'click on your username and change the email settings in your profile.\n\n'
            text_message += f'Thank you for using OICWebApps.com!\n\n'

            # Build the html message
            html_message = render_to_string(
                'kranich_skate_dates_email.html',
                {
                    'recipient_name': recipient.user.first_name,
                }
            )

            # Send email to each recipient separately
            try:
                mail = EmailMultiAlternatives(
                    subject, text_message, from_email, to_email
                )
                mail.attach_alternative(html_message, 'text/html')
                mail.send()
            except:
                return


if __name__ == "__main__":
    
    from_date = date.today() + timedelta(days=3)
    from_date = from_date.strftime("%m/%d/%Y")
    send_email = False

    # Every Thursday request schedule data and parse for Kranich Skate dates
    if date.today().weekday() == 3:
        get_schedule_data(from_date, from_date)

    if len(skate_dates) != 0:
        send_email = add_skate_dates(skate_dates)

    if send_email:
        add_john_to_skate()
        send_skate_dates_email()

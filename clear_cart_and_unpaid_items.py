###############################################################
#  This file to be run every day @ 1AM in a cron job or task  #
###############################################################

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OIC_Web_Apps.settings')

import django
django.setup()

from cart.models import Cart
from stickandpuck.models import StickAndPuckSession
# from thane_storck.models import SkateSession
from figure_skating.models import FigureSkatingSession
from adult_skills.models import AdultSkillsSkateSession
# from mike_schultz.models import MikeSchultzSkateSession
from yeti_skate.models import YetiSkateSession
from womens_hockey.models import WomensHockeySkateSession
from bald_eagles.models import BaldEaglesSession
from lady_hawks.models import LadyHawksSkateSession
# from chs_alumni.models import CHSAlumniSession
from private_skates.models import PrivateSkateSession
from kranich.models import KranichSkateSession
from nacho_skate.models import NachoSkateSession
from ament.models import AmentSkateSession
from accounts.models import UserCredit

from datetime import date

def clear_cart_and_unpaid_items():
    '''Clears bailed shopping carts and unpaid memberships, stick and puck sessions and open hockey sessions.'''

    todays_date = date.today()

    Cart.objects.all().delete()
    StickAndPuckSession.objects.filter(paid=False, session_date__gte=todays_date).delete()
    # SkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    FigureSkatingSession.objects.filter(paid=False, session__skate_date__gte=todays_date).delete()
    AdultSkillsSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    # MikeSchultzSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    YetiSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    WomensHockeySkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    BaldEaglesSession.objects.filter(paid=False, session_date__skate_date__gte=todays_date).delete()
    LadyHawksSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    # CHSAlumniSession.objects.filter(paid=False, date__skate_date__gte=todays_date).delete()
    PrivateSkateSession.objects.filter(paid=False, skate_date__date__gte=todays_date).delete()
    KranichSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    NachoSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    AmentSkateSession.objects.filter(paid=False, skate_date__skate_date__gte=todays_date).delete()
    UserCredit.objects.filter(pending__gt=0).update(pending=0)
    return

if __name__ == '__main__':
    clear_cart_and_unpaid_items()

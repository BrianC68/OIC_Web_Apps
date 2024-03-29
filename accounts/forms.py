from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Profile, ReleaseOfLiability, ChildSkater, UserCredit


class UserCreateForm(UserCreationForm):
    '''Form used to sign up for a user account.'''

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'User Name'
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['email'].label = 'Email Address'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True


class ProfileForm(forms.ModelForm):
    '''Form used to update a users profile'''

    class Meta:
        model = Profile
        fields = ['user', 'stick_and_puck_email', 'figure_skating_email',
                 'adult_skills_email', 'yeti_skate_email', 
                 'womens_hockey_email', 'bald_eagles_email', 'lady_hawks_email',
                 'kranich_email', 'nacho_skate_email', 'ament_email', 'open_roller_email']
        widgets = {'user': forms.HiddenInput()}
        labels = {
            'stick_and_puck_email': 'Receive Stick and Puck emails.',
            'figure_skating_email': 'Receive Figure Skating emails.',
            # 'thane_storck_email': 'Receive Thane Storck Skate emails.',
            'adult_skills_email': 'Receive Adult Skills emails.',
            # 'mike_schultz_email': 'Receive Mike Schultz Skate emails.',
            'yeti_skate_email': 'Receive Yeti Skate emails.',
            'womens_hockey_email': 'Receive Womens Hockey Emails.',
            'bald_eagles_email': 'Receive Bald Eagles Skate Emails.',
            'lady_hawks_email': 'Receive Lady Hawks Skate Emails.',
            # 'chs_alumni_email': 'Receive CHS Alumni Skate Emails.',
            'kranich_email': 'Receive Kranich Skate Emails.',
            'nacho_skate_email': 'Receive Nacho Skate Emails.',
            'ament_email': 'Receive Ament Skate Emails.',
            'open_roller_email': 'Receive Roller Hockey Emails.',
        }


class ReleaseOfLiablityForm(forms.ModelForm):
    '''Form used for Release of Liability Agreement'''

    class Meta:
        model = ReleaseOfLiability
        fields = ['release_of_liability']
        labels = {
            'release_of_liability': 'By checking this box I AGREE to the Release of Liability'
        }


class CreateChildSkaterForm(forms.ModelForm):
    '''Form used to add child skaters to ChildSkater model.'''

    class Meta:
        model = ChildSkater
        fields = ['first_name', 'last_name', 'date_of_birth']
        # widgets = {'user': forms.HiddenInput()}
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth'
        }
        help_texts = {
            'date_of_birth': 'mm/dd/yyyy',
        }


class CreateUserCreditForm(forms.ModelForm):
    '''Form used to purchase user credits.'''

    class Meta:
        model = UserCredit
        fields = ['pending']
        labels = {
            'pending': ''
        }

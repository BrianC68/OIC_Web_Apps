from django import forms
from stickandpuck.models import StickAndPuckSkaters, StickAndPuckSessions
from django.contrib.auth import get_user_model
User = get_user_model()

class StickAndPuckSkaterForm(forms.ModelForm):
    '''Displays page with form where users can add minor skaters to their account'''
    
    class Meta:
        model = StickAndPuckSkaters
        fields = ('first_name', 'last_name', 'date_of_birth')
        help_texts = {
            'date_of_birth': 'mm/dd/yyyy',
        }
        

class StickAndPuckSignupForm(forms.ModelForm):
    '''Displays page where users can sign up for stick and puck sessions'''

    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        
        self.fields['skater'].queryset = StickAndPuckSkaters.objects.filter(guardian=self.user)
    

    class Meta:
        model = StickAndPuckSessions
        fields = ('skater', 'session_date', 'session_time')

# class StickAndPuckSignupForm(forms.ModelForm):
#     '''Displays page where users can sign up for stick and puck sessions'''

#     class Meta:
#         model = StickAndPuckSessions
#         fields = ('skater', 'session_date', 'session_time')
#         # exclude = ['skater']

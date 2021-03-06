from django.db import models, IntegrityError
from django.contrib.auth import get_user_model
User = get_user_model()

from programs.models import Program


class BaldEaglesSkateDate(models.Model):
    '''Model holds dates for the Bald Eagles skate.'''

    # Model Fields
    skate_date = models.DateField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)

    class Meta:
        #Default ordering skate_date descending
        ordering = ['skate_date']
        # Prevent duplicate dates
        unique_together = ['skate_date', 'start_time', 'end_time']
        verbose_name_plural = 'Bald Eagles skate dates'

    def __str__(self):
        return f"{self.skate_date}"


class BaldEaglesSession(models.Model):
    '''Model that stores skate session data.'''

    # Model Fields
    skater = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.ForeignKey(BaldEaglesSkateDate, on_delete=models.CASCADE, related_name='session_skaters')
    goalie = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    class Meta:
        # Prevent duplicate entries
        unique_together = ['skater', 'session_date']
        # Default ordering date descending
        ordering = ['-session_date']
        verbose_name_plural = 'Bald Eagles sessions'

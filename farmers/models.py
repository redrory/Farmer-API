from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
GENDER_CHOICES = (
              ('Male', 'Male'),
              ('Female', 'Female'),
)


class Farmer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=15)
    gender = models.CharField(choices=GENDER_CHOICES, default='Male', max_length=10)
    verified_date = models.DateField(auto_now=False, auto_now_add=False)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    registration_date = models.DateField(auto_now=False, auto_now_add=False)


    class Meta:
        ordering = ('created',)
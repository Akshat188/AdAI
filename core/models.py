from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Users(models.Model):
    phoneno = PhoneNumberField(blank=False,help_text='Contact phone number')
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    def __str__(self):
        return str(self.Mobile)
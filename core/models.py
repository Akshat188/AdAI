from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User,default="", on_delete=models.CASCADE)
    phoneno = PhoneNumberField(blank=False,help_text='Contact phone number', unique=True)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    def __str__(self):
        return str(self.Mobile)
    def natural_key(self):
        return (self.phoneno)

class UserFields(models.Model):
    type1 = 't1'
    type2 = 't2'
    type3 = 't3'
    business_choice = [
        (type1,'type1'),
        (type2,'type2'),
        (type3,'type3')
    ]

    plan1 = 'p1'
    plan2 = 'p2'
    plan3 = 'p3'
    business_plan = [
        (plan1,'plan1'),
        (plan2,'plan2'),
        (plan3,'plan3')
    ]
    username = models.ForeignKey(Users , to_field='phoneno',on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    business_name = models.CharField(max_length=30)
    business_address = models.CharField(max_length=50)
    business_type = models.CharField(max_length=2,choices=business_choice,default=type1)
    business_plan = models.CharField(max_length=2,choices=business_plan,default=plan1)
    #fb_id = models.CharField(max_length=30)
    #insta_id = models.CharField(max_length=30)

class user_images(models.Model):
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(Users , to_field='phoneno',on_delete=models.CASCADE)

class themes(models.Model):
    type1 = 't1'
    type2 = 't2'
    type3 = 't3'
    business_choice = [
        (type1,'type1'),
        (type2,'type2'),
        (type3,'type3')
    ]
    name = models.CharField(max_length=30)
    business_type = models.CharField(max_length=2,choices=business_choice,default=type1)

class designer(models.Model):
    username = models.CharField(max_length=30)
    contribution = models.IntegerField(default=0, blank=False)

class images(models.Model):
    image = models.ImageField(upload_to='images_theme')
    theme_id = models.ForeignKey(themes , to_field='id',on_delete=models.CASCADE)
    designer_id = models.ForeignKey(designer , to_field='id',on_delete=models.CASCADE)

class customer(models.Model):
    name = models.CharField(max_length=30)
    contact = PhoneNumberField(blank=False,help_text='Contact phone number')
    status = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey(Users , to_field='phoneno',on_delete=models.CASCADE)


class sent_status(models.Model):
    business_id = models.ForeignKey(UserFields , to_field='id',on_delete=models.CASCADE)
    theme_id = models.ForeignKey(themes , to_field='id',on_delete=models.CASCADE)
    next_schedule = models.DateField()
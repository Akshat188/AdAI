from django.contrib.auth.backends import BaseBackend
from .models import Users
import pyotp
class MyBackend(BaseBackend):
    def authenticate(self, request, phoneno=None, otp=None):
        # Check the username/password and return a user.
        try:
            Mobile = Users.objects.get(phoneno=phoneno)
        except :
            return None  # False Call
        key='base32secret3232'
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        if OTP.verify(otp, Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            #token = Token.objects.create(user=)
            return Mobile
        return None
    
    def get_user(self, phoneno):
        try:
            return Users.objects.get(phoneno=phoneno)
        except :
            return None
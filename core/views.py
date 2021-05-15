from django.shortcuts import render
from django.http import HttpResponse
import json

from pyotp import otp
from .models import Users
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import base64
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class generate(APIView):
    # Get to Create a call for OTP
    def post(self,request,format=None):
        print("hello")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body['phone']
        try:
            Mobile = Users.objects.get(phoneno=phone)  # if Mobile already exists the take this else create New One
        except Users.DoesNotExist:
            key='base32secret3232'
            OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
            print(OTP.at(1))
            newuser = User(
                        username=phone,
                        password=OTP.at(1),
            )
            newuser.save()
            #Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
            client = Client("ACb28e5eba5a6ae96f29d738f8f4e6cfb6","f40cef9eab1fae1bea9044fd8f4a9917")
            client.messages.create(to=phone, 
                        from_="+17343597064", 
                        body=str(OTP.at(1)))
            Mobile = Users.objects.create(phoneno=phone,user=newuser)
            Mobile = Users.objects.get(phoneno=phone)  # user Newly created Model
            Mobile.counter +=1
            Mobile.save()
            return Response("Success") # Just for demonstration

            
        Mobile = Users.objects.get(phoneno=phone)  # user Newly created Model
        Mobile.counter +=1
        Mobile.save()
        key='base32secret3232'
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        newuser = User(
                    username=phone,
                    password=OTP.at(Mobile.counter),
        )
        Mobile.user=newuser
        #Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        client = Client("ACb28e5eba5a6ae96f29d738f8f4e6cfb6","f40cef9eab1fae1bea9044fd8f4a9917")
        client.messages.create(to=phone, 
                       from_="+17343597064", 
                       body=str(OTP.at(Mobile.counter)))
        
        return Response("Success") # Just for demonstration

class verify(APIView):    
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body['phone']
        try:
            Mobile = Users.objects.get(phoneno=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call
        key='base32secret3232'
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            user = Mobile.user
            token, created = Token.objects.get_or_create(user=user)
            data={}
            data['token']=token.key
            #token = Token.objects.create(user=)
            return Response(data,status=200)
        
        return Response("OTP is wrong", status=400)
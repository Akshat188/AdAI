from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.core import serializers
from PIL import Image
import base64
import time
import threading

from pyotp import otp
from .models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import base64
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

from threading import Timer
# Create your views here.

def OTPtimer(Mobile):
    threading.Timer(10, OTPtimer, [Mobile]).start()
    Mobile.counter +=1
    Mobile.save()
    

def check(usr):
    while(1):
        print(usr.counter)
        time.sleep(2)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class generate(APIView):
    # Get to Create a call for OTP
    def post(self,request,format=None):
        print("hello")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body['phone']
        phone = str(phone)
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
            
            #Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
            client = Client("ACb28e5eba5a6ae96f29d738f8f4e6cfb6","f40cef9eab1fae1bea9044fd8f4a9917")
            client.messages.create(to=phone, 
                        from_="+17343597064", 
                        body=str(OTP.at(1)))
            newuser.save()
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
        t.start()
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

class put_user_details(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body['phone']
        phone = str(phone)
        user = Users.objects.get(phoneno=phone)
        usr_detail = UserFields.objects.create(
            username = user,
            first_name = body['fname'],
            last_name = body['lname'],
            business_name = body['bname'],
            business_address = body['b_addr'],
            business_type = body['b_type'],
            business_plan = body['b_plan'],
            fb_id = body['fb_id'],
            insta_id = body['insta_id'],
            )
        return Response("Success")      

class get_user_details(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        phone = body['phone']
        phone = str(phone)
        try:
            Mobile = UserFields.objects.get(username=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call  
        data = serializers.serialize( "json", [ Mobile ] )
        return Response(data,status=200)

class put_theme(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theme = themes.objects.create(
            name = body['name'],
            business_type = body['b_type'],
            )
        return Response("Success")

class put_designer(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        theme = designer.objects.create(
            username = body['name']
            )
        return Response("Success")

class get_designer(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        uname = body['username']
        try:
            Mobile = designer.objects.filter(username=uname)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call  
        data = serializers.serialize( "json",  Mobile  )
        return Response(data,status=200)

class put_customer(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        userfield = UserFields.objects.get(id=body['b_id'])
        custom = customer.objects.create(
            name = body['name'],
            contact = body['contact'],
            business_id = userfield
            )
        return Response("Success")

class get_customer(APIView):
    def post(self,request,format=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        name = body['name']
        try:
            Mobile = customer.objects.filter(name=name)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call  
        data = serializers.serialize( "json",  Mobile  )
        return Response(data,status=200)

class put_user_images(APIView):
    parser_classes = (MultiPartParser, FormParser,FileUploadParser, )

    def post(self,request,format=None):
        img = Image.open(request.data['file'])
        user = Users.objects.get(phoneno=request.data['user'])
        usr_img = user_images.objects.create(
                user = user,
                image = request.data['file']
            )
        return Response({"mode": img.mode, "size": img.size, "format": img.format})

class put_images(APIView):
    parser_classes = (MultiPartParser, FormParser,FileUploadParser, )

    def post(self,request,format=None):
        img = Image.open(request.data['file'])
        theme = themes.objects.get(id=int(request.data['t_id']))
        design = designer.objects.get(id=int(request.data['d_id']))
        usr_img = images.objects.create(
                theme_id = theme,
                designer_id = design,
                image = request.data['file']
            )
        return Response({"mode": img.mode, "size": img.size, "format": img.format})

class get_user_images(APIView):
    def post(self,request,format=None):
        usr = Users.objects.get(phoneno=request.data['user'])
        images = user_images.objects.filter(user=usr)
        img_arr=[]
        root="media/"
        for img in images :
            path = root + str(img.image)
            with open(path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
                img_arr.append(image_data)
        return Response(img_arr)

class testapi(APIView):
    def post(self,request,format=None):
        usr = Users.objects.get(phoneno=request.data['user'])
        OTPtimer(usr)
        check(usr)
        return Response("succ")

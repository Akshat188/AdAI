from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('generate/',generate.as_view(), name='generate'),
    path('verify/',verify.as_view(),name='verify')
]
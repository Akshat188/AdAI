from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('generate/',generate.as_view(), name='generate'),
    path('verify/',verify.as_view(),name='verify'),
    path('put_user_details/',put_user_details.as_view(),name='put_user_details'),
    path('get_user_details/',get_user_details.as_view(),name='get_user_details'),
    path('put_theme/',put_theme.as_view(),name='put_theme'),
    path('put_designer/',put_designer.as_view(),name='put_designer'),
     path('get_designer/',get_designer.as_view(),name='get_designer'),
    path('put_customer/',put_customer.as_view(),name='put_customer'),
     path('get_customer/',get_customer.as_view(),name='get_customer'),
     path('put_user_images/',put_user_images.as_view(),name='put_user_images'),
     path('put_images/',put_images.as_view(),name='put_images'),
     path('get_user_images/',get_user_images.as_view(),name='get_user_images'),
     path('testapi/',testapi.as_view(),name='testapi'),
     path('random_photo/',random_photo.as_view(),name='random_photo'),
     path('update_user_details/',update_user_details.as_view(),name='update_user_details'),
     path('get_posters/',get_posters.as_view(),name='get_posters')
]
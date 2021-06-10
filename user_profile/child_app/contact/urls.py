from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/mail-u/', views.MailViewU.as_view()),

    path('about/phone-c/', views.PhoneViewC.as_view()),
    path('about/phone-ud/<int:pk>/', views.PhoneViewUD.as_view()),

    path('about/address-c/', views.AddressViewC.as_view()),
    path('about/address-ud/<int:pk>/', views.AddressViewUD.as_view()),
]

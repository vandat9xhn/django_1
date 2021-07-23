from django.urls import path
#
from . import views

#


urlpatterns = [
    path('phone-lap-l', views.PhoneLapViewL.as_view()),
    path('phone-lap-r', views.PhoneLapViewR.as_view()),
    path('vid-pic-l', views.VidPicViewL.as_view()),
    path('order-c', views.OrderViewC.as_view()),
]

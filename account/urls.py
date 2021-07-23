from django.urls import path
#
from . import views

#


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('define-user/', views.define_user),
    path('refresh-token/', views.CustomTokenRefreshView.as_view()),
]

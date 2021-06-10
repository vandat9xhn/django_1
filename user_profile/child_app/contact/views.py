from django.contrib.auth import authenticate
#
from rest_framework.response import Response
from rest_framework import status
#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView, UserUpdateOnlyOne
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class MailView:
    serializer_class = serializers.MailSerializer
    queryset = models.MailModel


class PhoneView:
    serializer_class = serializers.PhoneSerializer
    queryset = models.ProfileModel


class AddressView:
    serializer_class = serializers.AddressSerializer
    queryset = models.AddressModel


# -------------------------


#
class MailViewU(MailView, UserUpdateOnlyOne):

    def update(self, request, *args, **kwargs):
        password = request.data.get('password')
        username = request.user.username

        if authenticate(username=username, password=password):
            return super().update(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)


#
class PhoneViewC(PhoneView, UserCreateView):
    pass


class PhoneViewUD(PhoneView, UserUpdateView, UserDestroyView):
    pass


#
class AddressViewC(AddressView, UserCreateView):
    pass


class AddressViewUD(AddressView, UserUpdateView, UserDestroyView):
    pass

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
from django.contrib.auth import settings
from rest_framework_simplejwt.settings import api_settings


#


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom
        token['name'] = user.id

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['life_time'] = api_settings.ACCESS_TOKEN_LIFETIME

        return data

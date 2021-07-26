from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, settings
from django.contrib.auth.models import User
#
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
#
from .models import RefreshTokenModel
from .serializers import CustomTokenObtainPairSerializer
#
from user_profile.models import ProfileModel, NameModel, PersonalSettingModel
from user_profile.child_app.picture.models import PictureModel, CoverModel
from user_profile.child_app.contact.models import MailModel
from user_profile.child_app.relation.models import RelationModel
from user_profile.child_app.basis.models import BirthModel, GenderModel, LanguageModel
from user_profile.child_app.you.models import HobbyModel, AboutYouModel
#
from _common.views.no_token import NoTokenView
from _common.some_defs.get_picture import get_profile_picture
#
import json
import jwt
from jwt.exceptions import DecodeError
from datetime import datetime


# Create your views here.


#


# 
def load_account_from_cookie(cookie_str):
    try:
        account_obj = jwt.decode(cookie_str, settings.SECRET_KEY, 'HS256')
        username = account_obj.get(settings.LOGIN_USERNAME_KEY)
        password = account_obj.get(settings.LOGIN_PASSWORD_KEY)

        return username, password
    except DecodeError:
        return '', ''


def make_cookie_from_account(username, password):
    payload = {
        settings.LOGIN_USERNAME_KEY: username,
        settings.LOGIN_PASSWORD_KEY: password,
    }
    cookie_str = jwt.encode(payload, settings.SECRET_KEY, 'HS256')

    return cookie_str


#
def get_data_profile(user_id):
    name_model = NameModel.objects.get(profile_model=user_id)

    return {
        'id': user_id,
        'first_name': name_model.first_name,
        'last_name': name_model.last_name,
        'picture': get_profile_picture(user_id),
    }


# 
def get_validated_data(serializer):
    try:
        serializer.is_valid(raise_exception=True)
    except TokenError as e:
        raise InvalidToken(e.args[0])

    return serializer.validated_data


def get_serializer_from_account(username, password):
    return CustomTokenObtainPairSerializer(data={
        'username': username,
        'password': password,
    })


def get_data_save_refresh(serializer, refresh_model):
    validated_data = get_validated_data(serializer)
    refresh_token = validated_data.pop('refresh')
    refresh_model.refresh_token = refresh_token
    refresh_model.save()

    return validated_data


def get_data_save_refresh_from_account(username, password):
    serializer = CustomTokenObtainPairSerializer(data={
        'username': username,
        'password': password,
    })

    user_id = User.objects.get(username=username).id
    refresh_model = RefreshTokenModel.objects.get(profile_model=user_id)

    return get_data_save_refresh(serializer, refresh_model)


# 
def make_refresh_get_data(username, password, profile_model):
    serializer = get_serializer_from_account(username, password)
    validated_data = get_validated_data(serializer)
    refresh_token = validated_data.pop('refresh')

    RefreshTokenModel.objects.create(
        profile_model=profile_model,
        refresh_token=refresh_token,
    )

    return validated_data


#


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):

    def post(self, request, *args, **kwargs):
        cookie_str = request.COOKIES.get(settings.LOGIN_COOKIE_KEY)

        if not cookie_str:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        username, password = load_account_from_cookie(cookie_str)
        user = authenticate(username=username, password=password)

        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        refresh_model = RefreshTokenModel.objects.get(profile_model=user.id)

        refresh_time_life = api_settings.REFRESH_TOKEN_LIFETIME.total_seconds()
        refresh_time_existed = datetime.now().timestamp() - refresh_model.updated_time.timestamp()

        if refresh_time_existed <= refresh_time_life:
            serializer = get_serializer_from_account(username, password)
            validated_data = get_data_save_refresh(serializer, refresh_model)
        else:
            serializer = self.get_serializer(data={
                'refresh': refresh_model.refresh_token
            })
            validated_data = get_validated_data(serializer)
            validated_data.pop('refresh')

        return Response(validated_data, status=status.HTTP_200_OK)


#
def login(request):
    if request.method != 'POST':
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if not user:
        return HttpResponse('Wrong')

    auth_login(request, user)

    validated_data = get_data_save_refresh_from_account(username, password)

    response = HttpResponse(json.dumps({
        'access': validated_data['access'],
        'life_time': validated_data['life_time'].total_seconds(),
        **get_data_profile(user.id)
    }))
    response.set_cookie(
        key=settings.LOGIN_COOKIE_KEY,
        value=make_cookie_from_account(username, password),
        httponly=True
    )

    return response


def logout(request):
    auth_logout(request)

    return HttpResponse('')


#
def define_user(request):
    # print(request.session.get('_auth_user_hash'))
    if request.user.id:
        return HttpResponse(json.dumps(
            get_data_profile(request.user.id)
        ))

    username, password = load_account_from_cookie(request.COOKIES.get(settings.LOGIN_COOKIE_KEY))
    user = authenticate(username=username, password=password)

    if not user:
        return HttpResponse('Not Login')

    return HttpResponse(json.dumps(
        get_data_profile(user.id)
    ))


#
class RegisterView(NoTokenView, CreateAPIView):

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        gender = request.data['gender']
        year = request.data['year']
        month = request.data['month']
        day = request.data['day']

        if User.objects.filter(username=username).exists():
            return Response('Username has been existed')

        if User.objects.filter(email=email).exists():
            return Response('Email has been existed')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        user_id = user.id

        profile_model = ProfileModel.objects.create(
            id=user_id,
            is_online=True,
        )
        NameModel.objects.create(
            profile_model=profile_model,
            first_name=first_name,
            last_name=last_name,
        )
        PersonalSettingModel.objects.create(
            profile_model=profile_model,
        )

        # PictureModel.objects.create(
        #     profile_model=profile_model,
        # )
        # CoverModel.objects.create(
        #     profile_model=profile_model,
        # )

        MailModel.objects.create(
            profile_model=profile_model,
            mail=email,
        )

        BirthModel.objects.create(
            profile_model=profile_model,
            birth=datetime(int(year), int(month), int(day)),
        )
        GenderModel.objects.create(
            profile_model=profile_model,
            gender=gender,
        )
        LanguageModel.objects.create(
            profile_model=profile_model,
            lang='',
        )

        RelationModel.objects.create(
            profile_model=profile_model,
            relation='',
        )

        HobbyModel.objects.create(
            profile_model=profile_model,
            hobby='',
        )
        AboutYouModel.objects.create(
            profile_model=profile_model,
            you='',
        )

        validated_data = make_refresh_get_data(username, password, profile_model)

        data = {
            **validated_data,
            'id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'picture': '',
        }

        return Response(data, status=status.HTTP_201_CREATED)

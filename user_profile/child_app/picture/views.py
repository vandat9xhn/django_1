#
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
#
from . import serializers
from . import models
#
from _common.views.user_delete import UserDestroyView
from _common.views.active_view import change_active_instance
from _common.views.facebook.post import FollowPostViewL


# Create your views here.


# ------------- COMMON -----------


class PictureView:
    queryset = models.PictureModel.objects.all()
    serializer_class = serializers.PictureSerializer


class CoverView:
    queryset = models.CoverModel.objects.all()
    serializer_class = serializers.CoverSerializer


# ------------ COMMON -----------


class PictureCoverActiveViewU(UpdateAPIView):

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = request.user.id

        if user_id != instance.profile_model.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        change_active_instance(self.queryset.filter(profile_model=user_id))
        instance.is_active = True
        instance.save()

        return Response(status=status.HTTP_200_OK)


# -----------------------


#
class PictureViewL(PictureView, FollowPostViewL):
    pass


class PictureViewUD(PictureView, PictureCoverActiveViewU, UserDestroyView):
    pass


#
class CoverViewL(CoverView, FollowPostViewL):
    pass


class CoverViewUD(CoverView, PictureCoverActiveViewU, UserDestroyView):
    pass

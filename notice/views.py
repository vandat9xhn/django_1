from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView
#
from . import models, serializers

# Create your views here.

# ---------


class NoticeView:
    queryset = models.NoticeModel.objects.all()
    serializer_class = serializers.NoticeSerializer


# ----------


class NoticeViewL(NoticeView, ListAPIView):

    def get_queryset(self):
        return self.queryset.filter(profile_model=self.request.user.id)


class NoticeCountNewView(NoticeView, ListAPIView):

    def get(self, request, *args, **kwargs):
        count_new = self.queryset.filter(profile_model=request.user.id, status_seen=0).count()

        return Response(count_new)


class NoticeViewU(NoticeView, UpdateAPIView):

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.profile_model.id != request.user.id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        status_seen = request.data.get('status_seen')
        instance.status_seen = int(status_seen)
        instance.save()

        return Response(status=status.HTTP_200_OK)

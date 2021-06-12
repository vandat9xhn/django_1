from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.facebook.post import FollowPostViewL

# --------------


class HistoryView:
    queryset = models.HistoryModel.objects.all()
    serializer_class = serializers.HistorySerializer


# --------------


class HistoryViewL(HistoryView, FollowPostViewL):
    pass

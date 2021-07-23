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

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter more permission

        return queryset

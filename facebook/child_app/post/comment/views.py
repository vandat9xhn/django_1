from rest_framework.generics import ListAPIView
#
from .serializers import CommentSerializer, CommentModel, CmtLikeSerializer, CmtLikeModel, \
    CmtHistorySerializer, CmtHistoryModel
#
from _common.views.user_create import UserCreateView

# Create your views here.


#


class CommentViewLC(ListAPIView, UserCreateView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer


#


class CmtLikeViewL(ListAPIView):
    queryset = CmtLikeModel.objects.all()
    serializer_class = CmtLikeSerializer


#


class CmtHistoryViewL(ListAPIView):
    queryset = CmtHistoryModel.objects.all()
    serializer_class = CmtHistorySerializer

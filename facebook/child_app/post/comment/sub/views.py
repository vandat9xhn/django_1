from rest_framework.generics import ListAPIView
#
from .serizializers import SubSerializer, SubModel, SubLikeSerializer, SubLikeModel, \
    SubHistorySerializer, SubHistoryModel
#
from _common.views.user_create import UserCreateView

# Create your views here.


#


class SubViewLC(ListAPIView, UserCreateView):
    queryset = SubModel.objects.all()
    serializer_class = SubSerializer


#


class SubLikeViewL(ListAPIView):
    queryset = SubLikeModel.objects.all()
    serializer_class = SubLikeSerializer


#


class SubHistoryViewL(ListAPIView):
    queryset = SubHistoryModel.objects.all()
    serializer_class = SubHistorySerializer

from rest_framework.generics import ListAPIView
#
from .serializers import PostSerializer, PostModel

#


class PostViewL(ListAPIView):
    queryset = PostModel.objects.all().order_by('-updated_time')
    serializer_class = PostSerializer

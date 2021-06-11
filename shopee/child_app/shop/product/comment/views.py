from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from . import models, serializers
#
from _common.views.user_create import UserCreateView
from _common.views.no_token import NoTokenView


# Create your views here.


# -----------------
class ProductCmtView:
    queryset = models.ProductCmtModel.objects.all()
    serializer_class = serializers.ProductCmtSerializer


# ----------------


#
class ProductCmtViewL(ProductCmtView, NoTokenView, ListAPIView):

    def get_queryset(self):
        product_model = self.request.query_params.get('product_model')

        return self.queryset.filter(product_model=product_model)


class ProductCmtViewC(ProductCmtView, UserCreateView):

    def create(self, request, *args, **kwargs):
        profile_id = request.user.id
        product_model = request.data.get('product_model')
        content = request.data.get('content')
        vid_pics = request.data.getlist('vid_pics')

        if not content and len(vid_pics) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            'profile_model': profile_id,
            'product_model': product_model,
            'content': content,
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment_model = serializer.save()

        for vid_pic in vid_pics:
            vid_pic_model = models.ProductCmtVidPicModel(comment_model=comment_model, vid_pic=vid_pic)
            vid_pic_model.full_clean()
            vid_pic_model.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

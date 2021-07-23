from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer, DataSerializerL
from _common.serializers.content_field import ContentFieldSerializer
#
from . import models


#


class ProductCmtVidPicSerializer(FieldSerializer):
    name_field = 'product_cmt_vid_pics'
    #

    class Meta:
        model = models.ProductCmtVidPicModel
        fields = '__all__'


class ProductCmtSerializer(DataSerializerL, ContentFieldSerializer):
    name_field = 'product_cmt[]'
    #
    vid_pics = SerializerMethodField()
    content_obj = SerializerMethodField()

    class Meta:
        model = models.ProductCmtModel
        fields = '__all__'

    def get_vid_pics(self, instance):
        return self.get_data_l(
            ProductCmtVidPicSerializer,
            models.ProductCmtVidPicModel.objects.filter(comment_model=instance.id)
        )

    def get_content_obj(self, instance):
        return self.get_content_more('product_cmt', instance.content)

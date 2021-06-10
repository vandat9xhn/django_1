from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer, DataSerializerL
#
from . import models


#


class ProductCmtVidPicSerializer(FieldSerializer):
    name_field = 'product_cmt_vid_pics[]'
    #

    class Meta:
        model = models.ProductCmtVidPicModel
        fields = '__all__'


class ProductCmtSerializer(DataSerializerL):
    name_field = 'product_cmts[]'
    #
    vid_pics = SerializerMethodField('get_vid_pics')

    class Meta:
        model = models.ProductCmtModel
        fields = '__all__'

    def get_vid_pics(self, instance):
        return self.get_data_l(
            ProductCmtVidPicSerializer,
            models.ProductCmtVidPicModel.objects.filter(comment_model=instance.id)
        )

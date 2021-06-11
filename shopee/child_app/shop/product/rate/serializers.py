from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.content_field import ContentFieldSerializer
#
from . import models


#


class ProductRateSerializer(ContentFieldSerializer):
    name_field = 'product_rate[]'
    #
    content_obj = SerializerMethodField()

    class Meta:
        model = models.ProductRateModel
        fields = '__all__'

    def get_content_obj(self, instance):
        return self.get_content_more('product_rate', instance.content)

from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.content_field import ContentFieldSerializer
from _common.serializers.data_user import DataProfileSerializer
#
from . import models


#


class ProductRateSerializer(ContentFieldSerializer, DataProfileSerializer):
    name_field = 'product_rate'
    #
    content_obj = SerializerMethodField()

    class Meta:
        model = models.ProductRateModel
        fields = '__all__'

    def get_content_obj(self, instance):
        return self.get_content_more(instance.content)

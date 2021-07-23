#
from .models import PictureModel, CoverModel
#
from _common.serializers import data_field


#


class PictureSerializer(data_field.DataSerializerR):
    name_field = 'pf_pictures'
    #

    class Meta:
        model = PictureModel
        fields = '__all__'


class CoverSerializer(data_field.DataSerializerR):
    name_field = 'pf_covers'
    #

    class Meta:
        model = CoverModel
        fields = '__all__'

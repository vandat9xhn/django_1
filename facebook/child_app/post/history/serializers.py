from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import ArrCountSerializer, FieldSerializer
#
from .models import HistoryModel, HistoryVidPicCreateModel, HistoryVidPicDelModel

#


class HistoryVidPicCreateSerializer(FieldSerializer):
    name_field = 'create_histories[]'

    class Meta:
        model = HistoryVidPicCreateModel
        fields = '__all__'


class HistoryVidPicDelSerializer(FieldSerializer):
    name_field = 'del_histories[]'

    class Meta:
        model = HistoryVidPicDelModel
        fields = '__all__'


class HistorySerializer(ArrCountSerializer):
    name_field = 'histories[]'
    #
    del_obj = SerializerMethodField('get_del_obj')
    create_obj = SerializerMethodField('get_create_obj')

    class Meta:
        model = HistoryModel
        fields = '__all__'

    def get_del_obj(self, instance):
        return self.get_arr_count(
            HistoryVidPicDelSerializer,
            HistoryVidPicDelModel.objects.filter(his_model=instance.id),
            'vid_pic_del'
        )

    def get_create_obj(self, instance):
        return self.get_arr_count(
            HistoryVidPicCreateSerializer,
            HistoryVidPicCreateModel.objects.filter(his_model=instance.id),
            'vid_pic_del'
        )

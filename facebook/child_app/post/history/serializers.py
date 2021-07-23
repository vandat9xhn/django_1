from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import ArrCountSerializer, FieldSerializer
#
from .models import HistoryModel, HistoryVidPicCreateModel, HistoryVidPicDelModel

#


class HistoryVidPicCreateSerializer(FieldSerializer):
    name_field = 'history_creates'

    class Meta:
        model = HistoryVidPicCreateModel
        fields = '__all__'


class HistoryVidPicDelSerializer(FieldSerializer):
    name_field = 'history_del[]'

    class Meta:
        model = HistoryVidPicDelModel
        fields = '__all__'


class HistorySerializer(ArrCountSerializer):
    name_field = 'historys'
    #
    del_obj = SerializerMethodField()
    create_obj = SerializerMethodField()

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
            'vid_pic_create'
        )

from rest_framework.serializers import SerializerMethodField
#
from .models import SubModel, SubLikeModel, SubHistoryModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer


#


#


class SubLikeSerializer(FieldSerializer):
    name_field = 'sub_like[]'

    #

    class Meta:
        fields = '__all__'
        model = SubLikeModel


class SubHistorySerializer(FieldSerializer):
    name_field = 'sub_history[]'

    #

    class Meta:
        fields = '__all__'
        model = SubHistoryModel


class SubSerializer(DataLikeSerializer):
    name_field = 'sub[]'
    #
    like_obj = SerializerMethodField()
    history_obj = SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = SubModel

    def get_like_obj(self, instance):
        return self.get_data_like(
            SubLikeSerializer,
            SubLikeModel.objects.filter(sub_model=instance.id),
            'sub_like',
        )

    def get_history_obj(self, instance):
        return self.get_arr_count(
            SubHistorySerializer,
            SubHistoryModel.objects.filter(sub_model=instance.id),
            'sub_his',
        )

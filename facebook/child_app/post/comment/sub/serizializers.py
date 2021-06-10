from rest_framework.serializers import SerializerMethodField
#
from .models import SubModel, SubLikeModel, SubHistoryModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer


#


#


class SubLikeSerializer(FieldSerializer):
    name_field = 'sub_likes[]'

    #

    class Meta:
        fields = '__all__'
        model = SubLikeModel


class SubHistorySerializer(FieldSerializer):
    name_field = 'sub_histories[]'

    #

    class Meta:
        fields = '__all__'
        model = SubHistoryModel


class SubSerializer(DataLikeSerializer):
    name_field = 'subs[]'
    #
    like_obj = SerializerMethodField('get_like_obj')
    history_obj = SerializerMethodField('get_history_obj')

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

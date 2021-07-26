from rest_framework.serializers import SerializerMethodField
#
from . import models
#
from _common.serializers.custom_field import FieldSerializer

#


class OrderSerializer(FieldSerializer):
    name_field = 'phone_lap_order'

    class Meta:
        model = models.OrderModel
        fields = '__all__'


class VidPicSerializer(FieldSerializer):
    name_field = 'phone_lap_vid_pic'

    class Meta:
        model = models.VidPicModel
        fields = '__all__'


class PhoneLapSerializer(FieldSerializer):
    name_field = 'phone_lap'
    #
    vid_pics = SerializerMethodField()
    url = SerializerMethodField()

    class Meta:
        model = models.PhoneLapModel
        fields = '__all__'

    def get_vid_pics(self, instance):
        queryset = models.VidPicModel.objects.filter(phone_lap_model=instance.id)

        return {
            'data': VidPicSerializer(
                instance=queryset,
                many=True,
                context=self.context
            ).data[0:4],
            'count': queryset.count()
        }

    @staticmethod
    def get_url(instance):
        vid_pic_queryset = models.VidPicModel.objects.filter(phone_lap_model=instance.id)

        if vid_pic_queryset.exists():
            return vid_pic_queryset.first().vid_pic.url

        return ''

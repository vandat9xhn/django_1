from django.db.models import Sum
#
from _common.serializers.custom_field import FieldSerializer


# -------------


class DataSerializerL(FieldSerializer):

    def get_data_l(self, serializer_class, queryset, field=None):
        request = self.context['request']

        if not field:
            return serializer_class(
                instance=queryset,
                many=True,
                context={'request': request}
            ).data

        c_count = request.query_params.get(f'{field}_c_count')
        size = request.query_params.get(f'{field}_size')

        if not c_count:
            c_count = 0
        else:
            c_count = int(c_count)

        if not size:
            size = 10
        else:
            size = int(size)

        return serializer_class(
            instance=queryset,
            many=True,
            context={'request': request}
        ).data[c_count:size]


class DataSerializerR(FieldSerializer):

    def get_data_r(self, serializer_class, queryset):
        request = self.context['request']

        return serializer_class(
            instance=queryset,
            many=False,
            context={'request': request}
        ).data


# -------------


class ArrCountSerializer(DataSerializerL):

    def get_arr_count(self, serializer, queryset, field):
        request = self.context['request']

        if not request.query_params.get(field):
            return {
                'data': [],
                'count': queryset.count()
            }

        return {
            'data': self.get_data_l(serializer, queryset, field),
            'count': queryset.count()
        }


class DataLikeSerializer(ArrCountSerializer):

    def get_data_like(self, serializer, queryset, field):
        user = self.context['request'].user
        user_type_like = -1
        if user:
            if queryset.filter(profile_model=user.id).exists():
                user_type_like = queryset.get(profile_model=user.id).type_like

        return {
            **self.get_arr_count(serializer, queryset, field),
            'user_type_like': user_type_like,
        }


class DataShareSerializer(ArrCountSerializer):

    def get_data_share(self, serializer, queryset, field):
        user_count_share = 0
        user = self.context['request'].user
        if user:
            user_count_share = queryset.filter(profile_model=user.id)

        return {
            **self.get_arr_count(serializer, queryset, field),
            'user_count_share': user_count_share,
            'total_share': sum(queryset.values_list('count'))
        }


class DataLikeShareSerializer(DataLikeSerializer, DataShareSerializer):
    pass

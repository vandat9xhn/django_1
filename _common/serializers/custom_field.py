from rest_framework.serializers import ModelSerializer


#


class FieldSerializer(ModelSerializer):
    name_field = ''

    def get_field_names(self, declared_fields, info):
        fields = self.context['request'].query_params.getlist(self.name_field)
        if fields:
            return fields

        return super().get_field_names(declared_fields, info)

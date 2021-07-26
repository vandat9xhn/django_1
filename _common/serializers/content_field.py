from _common.serializers.custom_field import FieldSerializer

#


class ContentFieldSerializer(FieldSerializer):

    def get_content_more(self, content):
        if self.context['request'].query_params.get('has_more_content') is not None:
            return {
                'content': content[100:],
                'has_more_content': False
            }

        return {
            'content': content[0:100],
            'has_more_content': len(content) > 100
        }

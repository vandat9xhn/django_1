from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.no_token import NoTokenView


# Create your views here.


# --------------


class ProductView:
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


# ---------------------


#
class ProductViewL(ProductView, NoTokenView, ListAPIView):

    def get_queryset(self):
        type_request = self.request.query_params.get('type_request')

        if type_request == 'home':
            return self.queryset.all()

        if type_request == 'shop':
            # search = self.request.query_params.get('search')
            group_id = self.request.query_params.get('group')

            # if search is None:
            #     search = ''

            shop_id = self.request.query_params.get('shop_model')

            if group_id:
                return self.queryset.filter(
                    shop_model=shop_id,
                    group_model=group_id,
                    # search__contains=search
                )

            return self.queryset.filter(
                shop_model=shop_id,
                # search__contains=search
            )

        if type_request == 'search':
            search = self.request.query_params.get('search')
            areas = self.request.query_params.getlist('area')
            rate = self.request.query_params.get('rate') or 0
            sort_by = self.request.query_params.get('sort')

            areas_regex = '.*(' + '|'.join(areas) + ').*'

            return self.queryset.filter(
                name__contains=search,
                shop_model__address__regex=areas_regex,
                rate__gte=rate,
            ).sort_by(sort_by)

        if type_request == 'other_of_shop':
            shop_model = self.request.query_params.get('shop_model')
            product_id = self.request.query_params.get('product_model')

            return self.queryset.filter(shop_model=shop_model).exclude(id=product_id)

        if type_request == 'relative':
            product_id = self.request.query_params.get('product_model')
            product_model = models.ProductModel.objects.get(id=product_id)
            type_product = product_model.type

            return self.queryset.filter(type=type_product).exclude(id=product_id)

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

#


class HandlePagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'

    def paginate_queryset(self, queryset, request, view=None):
        c_count = request.query_params.get('c_count') or 0
        return super().paginate_queryset(queryset[int(c_count):], request, view=None)

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })

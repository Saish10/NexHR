__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from rest_framework.pagination import PageNumberPagination

class StandardPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    page_query_param = "page"
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return {
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "count": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "current_page": self.page.number,
            "results": data,
        }
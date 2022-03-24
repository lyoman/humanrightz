from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class ReportedCaseLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class ReportedCasePageNumberPagination(PageNumberPagination):
    page_size = 10
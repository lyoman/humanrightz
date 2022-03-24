from rest_framework.generics import ListAPIView

from report.models import ReportedCase, CompanyDetail
# from .serializers import ReportedCaseSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import ReportedCaseLimitOffSetPagination , ReportedCasePageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    ReportedCaseListSerializer,
    ReportedCaseDetailSerializer, 
    ReportedCaseCreateUpdateSerializer,

    CompanyDetailListSerializer,
    CompanyDetailDetailSerializer, 
    CompanyDetailCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class ReportedCaseListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class ReportedCaseCreateAPIView(CreateAPIView):
    queryset = ReportedCase.objects.all()
    serializer_class = ReportedCaseCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ReportedCaseUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ReportedCase.objects.all()
    serializer_class = ReportedCaseCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ReportedCaseDeleteAPIView(DestroyAPIView):
    queryset = ReportedCase.objects.all()
    serializer_class = ReportedCaseDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ReportedCaseDetailAPIView(RetrieveAPIView):
    queryset = ReportedCase.objects.all()
    serializer_class = ReportedCaseDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ReportedCaseListAPIView(ListAPIView):
    serializer_class = ReportedCaseListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = ReportedCasePageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ReportedCase.objects.filter(active=True)
        id = self.request.query_params.get('user', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
            print("hey you", queryset)
        return queryset



#Creating an CompanyDetail
class CompanyDetailCreateAPIView(CreateAPIView):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class CompanyDetailUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class CompanyDetailDeleteAPIView(DestroyAPIView):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class CompanyDetailDetailAPIView(RetrieveAPIView):
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class CompanyDetailListAPIView(ListAPIView):
    serializer_class = CompanyDetailListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # pagination_class = ReportedCasePageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = CompanyDetail.objects.filter()
        id = self.request.query_params.get('user', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
            print("hey you", queryset)
        return queryset


class CompanyDetailUserListAPIView(ListAPIView):
    serializer_class = CompanyDetailListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    # pagination_class = ReportedCasePageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = CompanyDetail.objects.filter()
        id = self.request.query_params.get('user', None)
        if id is not None:
            queryset = queryset.filter(user_id=id)
            print("hey you", queryset)
        return queryset
from psycopg2 import Timestamp
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

from django.http import JsonResponse
from rest_framework.views import APIView
from report.models import Victim, ReportedCase
from rest_framework.response import Response
from rest_framework import permissions, status
class CasesView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        cases = ReportedCase.objects.all()
        # objs = ReportedCaseListSerializer(cases, many=True).data
        # serializer = ReportedCaseListSerializer(data=request.data,context={'request': request})
        context_serializer = {
            'request': request
        }
        # return Response(objs, status=status.HTTP_200_OK, context=context_serializer)
        serializer = ReportedCaseListSerializer(cases, context=context_serializer)    
        return Response(serializer.data)
        
    def post(self, request):
        location = request.data["location"]
        type_of_violation = request.data["type_of_violation"]
        print(request.data)
        case = ReportedCase(
            location = location,
            type_of_violation = type_of_violation
        )
        case.save()

        for i in range(0, 100):
          try:
                victim_name = request.data[f"victim_name_{i}"]
                victim = Victim(
                    name = victim_name,
                    case=case
                )
                victim.save()
          except Exception as e:
              break
        return JsonResponse({"success": True})

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
        fromDate = self.request.query_params.get('fromDate',None)
        toDate = self.request.query_params.get('toDate',None)
        response  = ReportedCase.objects.filter(type_of_violation=fromDate,read_status=toDate, active=True)
        id = self.request.query_params.get('user', None)
        if id is not None:
            queryset = response.filter(user_id=id)
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
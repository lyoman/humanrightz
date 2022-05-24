from django.contrib import admin
from django.urls import path

from .views import (
    ReportedCaseListAPIView,
    ReportedCaseDeleteAPIView,
    ReportedCaseDetailAPIView,
    ReportedCaseUpdateAPIView,
    ReportedCaseCreateAPIView,

    CompanyDetailListAPIView,
    CompanyDetailDeleteAPIView,
    CompanyDetailDetailAPIView,
    CompanyDetailUpdateAPIView,
    CompanyDetailCreateAPIView,
    CompanyDetailUserListAPIView,

    # CasesView
	)

urlpatterns = [
    path('report_case/', ReportedCaseListAPIView.as_view(), name='list'),
    path('report_case/new/', ReportedCaseCreateAPIView.as_view(), name='new'),
    path('report_case/<int:id>/detail/', ReportedCaseDetailAPIView.as_view(), name='detail'),
    path('report_case/<int:id>/edit/', ReportedCaseUpdateAPIView.as_view(), name='update'),
    path('report_case/<int:id>/delete/', ReportedCaseDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('company/', CompanyDetailListAPIView.as_view(), name='company_list'),
    path('company_user/', CompanyDetailUserListAPIView.as_view(), name='company_detail_user'),
    path('company/new/', CompanyDetailCreateAPIView.as_view(), name='new_company'),
    path('company/<int:id>/detail/', CompanyDetailDetailAPIView.as_view(), name='company_detail'),
    path('company/<int:id>/edit/', CompanyDetailUpdateAPIView.as_view(), name='update_company'),
    path('company/<int:id>/delete/', CompanyDetailDeleteAPIView.as_view(), name="delete_company"),

    # new url
    # path('cases/', CasesView.as_view(), name='case'),

]

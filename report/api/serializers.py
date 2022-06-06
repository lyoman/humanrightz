from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from report.models import ReportedCase, CompanyDetail, MediaFile
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# class VictimSerializer(ModelSerializer):
#     class Meta:
#         model = Victim
#         fields = ("name", "phone", "address")

class ReportedCaseCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ReportedCase
        fields = [
        'id',
        "date_reported", 
        "type_of_violation", 
        "fd_how_many_removed", 
        "fd_alternative_place", 
        "fd_alternative_place_description", 
        "ep_what_kind", 
        "ep_source",
        "ep_source_description",
        "ep_num_people_exposed", 
        "ep_who_is_responsible",

        "ll_assests_lost", 
        "ll_who_is_responsible",
        "ll_families_affected", 

        "dc_how_many_graves", 
        "dc_who_desecrated_them",

        "ti_type", 
        "ti_other",
        "ti_groups_affected", 
        "ti_who_did_this", 
        "ti_company_involved",
        "ti_the_reason", 

        "rf_company_involved",

        "la_company_involved",

        "fu_company_involved", 

        "cl_company_involved",
        "cl_number_of_children", 

        "sv_affected_people",
        "sv_type", 
        "sv_company_involved",
        "sv_who_did_this",

        "mk_groups_of_persons", 
        "mk_number_of_people",
        "mk_how_they_died", 
        "mk_murder_other",
        "mk_company_involved", 

        "what_happened",

        "reporter_phone", 
        "reporter_address",
        "reporter_email", 

        "name_of_area", 
        "village",
        "chief", 
        "ward_name",
        "location",
        "district", 
        "province", 
        "latitude", 
        "longitude",

        "collection_vp", 
        "media_files",
        ]


reportcase_detail_url = HyperlinkedIdentityField(
        view_name='reportcase-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class ReportedCaseDetailSerializer(ModelSerializer):
    url = reportcase_detail_url
    class Meta:
        model = ReportedCase
        fields = [
            'url',
            'id',
            "date_reported", 
            "type_of_violation", 
            "fd_how_many_removed", 
            "fd_alternative_place", 
            "fd_alternative_place_description", 
            "ep_what_kind", 
            "ep_source",
            "ep_source_description",
            "ep_num_people_exposed", 
            "ep_who_is_responsible",

            "ll_assests_lost", 
            "ll_who_is_responsible",
            "ll_families_affected", 

            "dc_how_many_graves", 
            "dc_who_desecrated_them",

            "ti_type", 
            "ti_other",
            "ti_groups_affected", 
            "ti_who_did_this", 
            "ti_company_involved",
            "ti_the_reason", 

            "rf_company_involved",

            "la_company_involved",

            "fu_company_involved", 

            "cl_company_involved",
            "cl_number_of_children", 

            "sv_affected_people",
            "sv_type", 
            "sv_company_involved",
            "sv_who_did_this",

            "mk_groups_of_persons", 
            "mk_number_of_people",
            "mk_how_they_died", 
            "mk_murder_other",
            "mk_company_involved", 

            "what_happened",

            "reporter_phone", 
            "reporter_address",
            "reporter_email", 

            "name_of_area", 
            "village",
            "chief", 
            "ward_name",
            "location",
            "district", 
            "province", 
            "latitude", 
            "longitude",

            "collection_vp", 
            "media_files",

            "active",
            'updated',
            'timestamp'
        ]

class ReportedCaseListSerializer(serializers.ModelSerializer):
    url = reportcase_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='reportcase-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ReportedCase
        fields = [
            'url',
            'id',
            'delete_url',
            "date_reported", 
            "type_of_violation", 
            "fd_how_many_removed", 
            "fd_alternative_place", 
            "fd_alternative_place_description", 
            "ep_what_kind", 
            "ep_source",
            "ep_source_description",
            "ep_num_people_exposed", 
            "ep_who_is_responsible",

            "ll_assests_lost", 
            "ll_who_is_responsible",
            "ll_families_affected", 

            "dc_how_many_graves", 
            "dc_who_desecrated_them",

            "ti_type", 
            "ti_other",
            "ti_groups_affected", 
            "ti_who_did_this", 
            "ti_company_involved",
            "ti_the_reason", 

            "rf_company_involved",

            "la_company_involved",

            "fu_company_involved", 

            "cl_company_involved",
            "cl_number_of_children", 

            "sv_affected_people",
            "sv_type", 
            "sv_company_involved",
            "sv_who_did_this",

            "mk_groups_of_persons", 
            "mk_number_of_people",
            "mk_how_they_died", 
            "mk_murder_other",
            "mk_company_involved", 

            "what_happened",

            "reporter_phone", 
            "reporter_address",
            "reporter_email", 

            "name_of_area", 
            "village",
            "chief", 
            "ward_name",
            "location",
            "district", 
            "province", 
            "latitude", 
            "longitude",

            "collection_vp", 
            "media_files",
            "active",
            'updated',
            'timestamp'
        ]


# def create(self, validated_data):
#     user = self.context.get('user') #you can pass context={'user': self.request.user} in your view to the serializer
#     up = ReportedCase.objects.create(email_id=user)
#     up.save()        
#     preference = validated_data.get('preference', [])
#     up.preference.add(*preference)
#     up.save()
#     return up


#####Process flow Charts
class CompanyDetailCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    class Meta:
        model = CompanyDetail
        fields = [
            'id',
            'user',
            "owners", 
            "when_it_started_operating", 
            "description",
            "name", 
            "location"
        ]


soldstock_detail_url = HyperlinkedIdentityField(
        view_name='reportcase-api:company_detail',
        lookup_field='id'#or primary key <pk>
    )

class CompanyDetailDetailSerializer(ModelSerializer):
    url = soldstock_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = CompanyDetail
        fields = [
            'url',
            'id',
            'user',
            "owners", 
            "when_it_started_operating", 
            "description",
            "name", 
            "location", 
            'active',
            'updated',
            'timestamp'
        ]

class CompanyDetailListSerializer(ModelSerializer):
    url = soldstock_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='reportcase-api:delete_company',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = CompanyDetail
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            "owners", 
            "when_it_started_operating", 
            "description",
            "name", 
            "location", 
            'active',
            'updated',
            'timestamp'
        ]



class MediaFileCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = MediaFile
        fields = [
        'name',
        "file",
        "type", 
        ]
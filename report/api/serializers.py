from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from report.models import ReportedCase, CompanyDetail, Victim
# from .serializers import PostSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class VictimSerializer(ModelSerializer):
    class Meta:
        model = Victim
        fields = ("name", "phone", "address")

class ReportedCaseCreateUpdateSerializer(ModelSerializer):
    victims = serializers.SerializerMethodField()
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    # invoice        = models.ImageField(upload_to = user_directory_path)

    class Meta:
        model = ReportedCase
        fields = [
            'id',
            'victims',
            'experiment',
            'user',
            'company',
            "date_reported", 
            "type_of_violation", 
            "description_of_victims", 
            "description_of_perpetrator", 
            "motivations_behind_incident", 
            "what_happened", 
            "how_it_happened",
            "community_description",
            "evidence_files", 
            "location",
            "latitude", 
            "longitude",
            "identity_verification", 
        ]

    def get_victims(self, case):
        vctms = case.victims.all()
        return VictimSerializer(instance=vctms, many=True).data


reportcase_detail_url = HyperlinkedIdentityField(
        view_name='reportcase-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class ReportedCaseDetailSerializer(ModelSerializer):
    url = reportcase_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ReportedCase
        fields = [
            'url',
            'id',
            'user',
            "date_reported",
            'company',
            "type_of_violation", 
            "description_of_victims", 
            # "names_of_vitims", 
            # "victim_age", 
            # "victim_gender", 
            # "describe_gender", 
            # "victim_phone_number",
            # "victim_address", 
            "description_of_perpetrator", 
            "motivations_behind_incident", 
            "what_happened", 
            "how_it_happened",
            "community_description",
            "evidence_files", 
            "location",
            "latitude", 
            "longitude",
            "identity_verification", 
            "active",
            'updated',
            'timestamp'
        ]

class ReportedCaseListSerializer(serializers.ModelSerializer):
    url = reportcase_detail_url
    victims = VictimSerializer(many=True)
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='reportcase-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ReportedCase
        fields = [
            "victims",
            "experiment",
            'url',
            'user',
            'id',
            'delete_url',
            'company',
            "date_reported", 
            "type_of_violation", 
            "description_of_victims", 
            # "names_of_vitims", 
            # "victim_age", 
            # "victim_gender", 
            # "describe_gender", 
            # "victim_phone_number",
            # "victim_address", 
            "description_of_perpetrator", 
            "motivations_behind_incident", 
            "what_happened", 
            "how_it_happened",
            "community_description",
            "evidence_files", 
            "location",
            "latitude", 
            "longitude",
            "identity_verification", 
            "active",
            'updated',
            'timestamp'
        ]

        
    def get_victims(self, case):
            vctms = case.victims.all()
            return VictimSerializer(instance=vctms, many=True).data



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
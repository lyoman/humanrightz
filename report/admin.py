from django.contrib import admin
from . models import ReportedCase, CompanyDetail

# Register your models here.
class ReportedCaseModelAdmin(admin.ModelAdmin):
    list_display        = [
        "user",
        "active",
        "date_reported", 
        "type_of_violation", 
        "description_of_victims", 
        "names_of_vitims", 
        "victim_age", 
        "victim_gender", 
        "describe_gender", 
        "victim_phone_number",
        "victim_address", 
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
        "updated", 
        "timestamp",
        ]
    list_display_links  = ["updated", "timestamp", "user", "date_reported"]
    list_editable       = ["type_of_violation", "what_happened", "active"]
    list_filter         = ["updated", "timestamp", "location"]
    search_fields       = ["names_of_vitims", "location"]
    class Meta:
        model = ReportedCase

class CompanyDetailModelAdmin(admin.ModelAdmin):
    list_display        = [
                           "user", 
                           "owners", 
                           "when_it_started_operating", 
                           "description",
                           "name", 
                           "location", 
                           "timestamp", 
                           "updated"
                           ]
    list_display_links  = ["updated", "timestamp", "user", "location", "name"]
    list_editable       = ["owners"]
    list_filter         = ["updated", "timestamp", "when_it_started_operating"]
    search_fields       = ["description"]
    class Meta:
        model = CompanyDetail


admin.site.register(ReportedCase, ReportedCaseModelAdmin)
admin.site.register(CompanyDetail, CompanyDetailModelAdmin)
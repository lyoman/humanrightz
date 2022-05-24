from django.contrib import admin
from . models import ReportedCase, CompanyDetail

# Register your models here.
class ReportedCaseModelAdmin(admin.ModelAdmin):
    list_display        = [
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

        "es_which_resource",
        "es_who_is_smuggling", 
        "es_company_involved", 

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

        "identity_verification", 
        "evidence_files",
        "collection_vp", 
        "media_files",

        "active",

        "updated", 
        "timestamp"
        ]
    list_display_links  = ["updated", "timestamp", "date_reported", "name_of_area"]
    list_editable       = ["type_of_violation", "active", "province", "active"]
    list_filter         = ["updated", "timestamp", "location"]
    search_fields       = ["type_of_violation", "location"]
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

# @admin.register(Victim)
# class VictimAdmin(admin.ModelAdmin):
#     list_display = ('case', "name")
admin.site.register(ReportedCase, ReportedCaseModelAdmin)
admin.site.register(CompanyDetail, CompanyDetailModelAdmin)
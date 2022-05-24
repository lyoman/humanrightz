from statistics import mode
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

VIOLATION_TYPE = (
    ("Forced displacement", "Forced displacement"),
    ("Exposure to pollutants", "Exposure to pollutants"),
    ("Loss of land or economic assets", "Loss of land or economic assets"),
    ("Desecration of cultural heritage including graves", "Desecration of cultural heritage including graves"),
    ("Torture, intimidation and harassment", "Torture, intimidation and harassment"),
    ("Curtailed freedom of movement", "Curtailed freedom of movement"),
    ("Exposure to degraded environment", "Exposure to degraded environment"),
    ("Limited access to water", "Limited access to water"),
    ("Denied access to social services like Health facilities, School, Markets place", "Denied access to social services like Health facilities, School, Markets place"),
    ("Forced and unpaid labour", "Forced and unpaid labour"),
    ("Child labour", "Child labour"),
    ("Murder or killings", "Murder or killings"),
)

VICTIMS_DESCRIPTION = (
    ("Community member (individual/group)", "Community member (individual/group)"),
    ("Women", "Women"),
    ("Girls", "Girls"),
    ("Youth", "Youth"),
    ("Household", "Household"),
    ("Mining company", "Mining company"),
    ("Traditional leader", "Traditional leader"),
    ("Farmer", "Farmer"),
    ("Community activist", "Community activist"),
    ("School children", "School children"),
)

VICTIMS_GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
     ("", ""),
    ("Famale & Male", "Male & Female"),
    ("Both", "Both"),
)

PERPETRATOR_DESCRIPTION = (
    ("Member of Parliament", "Member of Parliament"),
    ("Mining company security guards", "Mining company security guards"),
    ("Artisanal miners ", "Artisanal miners "),
    ("Politician", "Politician"),
    ("Government security agencies", "Government security agencies"),
    ("Councilors", "Councilors"),
)

MOTIVATIONS_BEHIND = (
    ("Political", "Political"),
    ("To conceal illicit activities and corruption", "To conceal illicit activities and corruption"),
    ("To exercise power", "To exercise power"),
    ("To instill fear", "To instill fear"),
    ("Economic interest", "Economic interest"),
)

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class CompanyDetail(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    owners         = models.CharField(max_length=250, null=False, blank=False)
    when_it_started_operating = models.CharField(max_length=250, null=False, blank=False)
    description    = models.TextField(blank = True)
    name           = models.CharField(max_length=250, null=False, blank=False)
    location       = models.CharField(max_length=250, null=False, blank=False)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.location

    class Meta:
        ordering = ["-timestamp", "-updated"]
        

class ReportedCase(models.Model):
    evidence_files   = models.ImageField(upload_to = 'transpired_description/', blank=True, null=True)
    identity_verification = models.FileField(upload_to = 'identity_verification/', blank=True, null=True)
    # file_field     = models.FileField(widget=models.ClearableFileInput(attrs={'multiple': True}))

    date_reported= models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    type_of_violation      = models.CharField(max_length=250, choices=VIOLATION_TYPE, blank=True, null=True)

    #  // Forced Displacement
    fd_how_many_removed= models.CharField(max_length=250, blank=True, null=True)
    fd_alternative_place= models.CharField(max_length=250, blank=True, null=True)
    fd_alternative_place_description= models.CharField(max_length=250, blank=True, null=True)

    # //Exposure to pollutants
    ep_what_kind= models.CharField(max_length=250, blank=True, null=True)
    ep_source= models.CharField(max_length=250, blank=True, null=True)
    ep_source_description= models.CharField(max_length=250, blank=True, null=True)
    ep_num_people_exposed= models.CharField(max_length=250, blank=True, null=True)
    ep_who_is_responsible= models.CharField(max_length=250, blank=True, null=True)

    # // Loss of land or economic assets
    ll_assests_lost= models.CharField(max_length=250, blank=True, null=True)
    ll_who_is_responsible= models.CharField(max_length=250, blank=True, null=True)
    ll_families_affected= models.CharField(max_length=250, blank=True, null=True)

    # // Desecration of cultural heritage including graves
    dc_how_many_graves= models.CharField(max_length=250, blank=True, null=True)
    dc_who_desecrated_them= models.CharField(max_length=250, blank=True, null=True)

    # // Torture, intimidation and harassment
    ti_type= models.CharField(max_length=250, blank=True, null=True)
    ti_other= models.CharField(max_length=250, blank=True, null=True)
    ti_groups_affected= models.CharField(max_length=250, blank=True, null=True)
    ti_who_did_this= models.CharField(max_length=250, blank=True, null=True)
    ti_company_involved= models.CharField(max_length=250, blank=True, null=True)
    ti_the_reason= models.CharField(max_length=250, blank=True, null=True)

    # // Reduced freedom of movement
    rf_company_involved= models.CharField(max_length=250, blank=True, null=True)

    # // Limited access to water
    la_company_involved= models.CharField(max_length=250, blank=True, null=True)

    # // Forced and unpaid labour
    fu_company_involved= models.CharField(max_length=250, blank=True, null=True)

    # // Child labour
    cl_company_involved= models.CharField(max_length=250, blank=True, null=True)
    cl_number_of_children= models.CharField(max_length=250, blank=True, null=True)

    # // Evidence of smuggling
    es_which_resource= models.CharField(max_length=250, blank=True, null=True)
    es_who_is_smuggling= models.CharField(max_length=250, blank=True, null=True)
    es_company_involved= models.CharField(max_length=250, blank=True, null=True)

    # // Sexual violence
    sv_affected_people= models.CharField(max_length=250, blank=True, null=True)
    sv_type= models.CharField(max_length=250, blank=True, null=True)
    sv_company_involved= models.CharField(max_length=250, blank=True, null=True)
    sv_who_did_this= models.CharField(max_length=250, blank=True, null=True)

    # // Murder or killings
    mk_groups_of_persons= models.CharField(max_length=250, blank=True, null=True)
    mk_number_of_people= models.CharField(max_length=250, blank=True, null=True)
    mk_how_they_died= models.CharField(max_length=250, blank=True, null=True)
    mk_murder_other= models.CharField(max_length=250, blank=True, null=True)
    mk_company_involved= models.CharField(max_length=250, blank=True, null=True)


    what_happened= models.CharField(max_length=250, blank=True, null=True)

    reporter_phone= models.CharField(max_length=250, blank=True, null=True)
    reporter_address= models.CharField(max_length=250, blank=True, null=True)
    reporter_email= models.CharField(max_length=250, blank=True, null=True)

    # // location
    name_of_area= models.CharField(max_length=250, blank=True, null=True)
    village= models.CharField(max_length=250, blank=True, null=True)
    chief= models.CharField(max_length=250, blank=True, null=True)
    ward_name= models.CharField(max_length=250, blank=True, null=True)
    district= models.CharField(max_length=250, blank=True, null=True)
    province= models.CharField(max_length=250, blank=True, null=True)
    location= models.CharField(max_length=250, blank=True, null=True)
    latitude       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude      = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    # //Array
    collection_vp = models.JSONField(default=dict)
    media_files = models.JSONField(default=dict)


    active         = models.BooleanField(default=True)

    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.type_of_violation

    class Meta:
        ordering = ["-timestamp", "-updated"]


# class Victim(models.Model):
#     case = models.ForeignKey("report.ReportedCase", related_name="victims", on_delete=models.CASCADE)
#     name = models.CharField(_("Victim name"), max_length=200)
#     address = models.CharField(_("Victim address"), max_length=200)
#     phone =  models.CharField(_("Phone"), max_length=13)

#     def __str__(self):
#         return self.name




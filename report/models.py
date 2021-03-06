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


class MediaFile(models.Model):
    # evidence_files   = models.ImageField(upload_to = 'transpired_description/', blank=True, null=True)
    # identity_verification = models.FileField(upload_to = 'identity_verification/', blank=True, null=True)
    file = models.FileField(_("The actual file"), upload_to = 'evidence_files/', blank=True, null=True)
    name       = models.CharField(max_length=250, null=False, blank=False)
    type       = models.CharField(max_length=250, null=False, blank=False)
    updated    = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp  = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name + ' - ' + self.type

    class Meta:
        ordering = ["-timestamp", "-updated"]
        

class ReportedCase(models.Model):
    # file_field     = models.FileField(widget=models.ClearableFileInput(attrs={'multiple': True}))

    date_reported= models.DateTimeField(_("Date of incident"),auto_now=False, auto_now_add=False, blank=True, null=True)
    type_of_violation      = models.CharField(_("Type of violation"),max_length=250, choices=VIOLATION_TYPE, blank=True, null=True)

    #  // Forced Displacement
    fd_how_many_removed= models.CharField(_("How many people have been forcibly displaced?"),max_length=250, blank=True, null=True)
    fd_alternative_place= models.CharField(_("Have they been offered alternative places to stay?"),max_length=250, blank=True, null=True)
    fd_alternative_place_description= models.CharField(_("Have they been offered alternative places to stay (Optional description)"),max_length=250, blank=True, null=True)

    # //Exposure to pollutants
    ep_what_kind= models.CharField(_("What kind of pollution have they been exposed to?"),max_length=250, blank=True, null=True)
    ep_source= models.CharField(_("What is the source of the pollution?"),max_length=250, blank=True, null=True)
    ep_source_description= models.CharField(_("Optional description of source of pollution"),max_length=250, blank=True, null=True)
    ep_num_people_exposed= models.CharField(_("How many people have been exposed to this pollution?"),max_length=250, blank=True, null=True)
    ep_who_is_responsible= models.CharField(_("Who is responsible for the pollution (name of company)?"),max_length=250, blank=True, null=True)

    # // Loss of land or economic assets
    ll_assests_lost= models.CharField(_("What economic assets have you lost ? - livestock, agricultural land, other specify"),max_length=250, blank=True, null=True)
    ll_who_is_responsible= models.CharField(_("Who is responsible for the loss (company name)?"),max_length=250, blank=True, null=True)
    ll_families_affected= models.CharField(_("How many families were affected?"),max_length=250, blank=True, null=True)

    # // Desecration of cultural heritage including graves
    dc_how_many_graves= models.CharField(_("How many sites were desecrated?"),max_length=250, blank=True, null=True)
    dc_who_desecrated_them= models.CharField(_("Who desecrated them?"),max_length=250, blank=True, null=True)

    # // Torture, intimidation and harassment
    # ti_type= models.CharField(_("Type of torture, intimidation, harassment"),max_length=250, blank=True, null=True)
    ti_type = models.JSONField(_("Type of torture, intimidation, harassment"),default=dict, blank=True, null=True)
    ti_other= models.CharField(_("Other type of harassment"),max_length=250, blank=True, null=True)
    ti_groups_affected= models.CharField(_("Which groups of people were affected ?"),max_length=250, blank=True, null=True)
    ti_who_did_this= models.CharField(_("Who did this ?"),max_length=250, blank=True, null=True)
    ti_company_involved= models.CharField(_("Which company was involved ?"),max_length=250, blank=True, null=True)
    ti_the_reason= models.CharField(_("What did they say was the reason for this ?"),max_length=250, blank=True, null=True)

    # // Reduced freedom of movement
    rf_company_involved= models.CharField(_("Restricted freedom of movement (Which company was involved?)"),max_length=250, blank=True, null=True)

    # // Limited access to water
    la_company_involved= models.CharField(_("Limited access to water (Which company was involved?)"),max_length=250, blank=True, null=True)

    # // Forced and unpaid labour
    fu_company_involved= models.CharField(_("Forced and unpaid labour (Which company was involved?)"),max_length=250, blank=True, null=True)

    # // Child labour
    cl_company_involved= models.CharField(_("Child labour (Which company was involved?)"),max_length=250, blank=True, null=True)
    cl_number_of_children= models.CharField(_("Child labour (Number of children involved)"),max_length=250, blank=True, null=True)

    # // Sexual violence
    sv_affected_people= models.CharField(_("Sexual violence (Who is / are affected ?)"),max_length=250, blank=True, null=True)
    sv_type= models.CharField(_("Sexual violence (Type of sexual violence)"),max_length=250, blank=True, null=True)
    sv_company_involved= models.CharField(_("Sexual violence (Which company was involved ?)"),max_length=250, blank=True, null=True)
    sv_who_did_this= models.CharField(_("Sexual violence (Who did this?)"),max_length=250, blank=True, null=True)

    # // Murder or killings
    mk_groups_of_persons= models.CharField(_("Murder or killings (Groups of persons murdered)"),max_length=250, blank=True, null=True)
    mk_number_of_people= models.CharField(_("Murder or killings (Number of people killed)"),max_length=250, blank=True, null=True)
    mk_how_they_died= models.CharField(_("Murder or killings (How the people were killed)"),max_length=250, blank=True, null=True)
    mk_murder_other= models.CharField(_("Murder or killings (Description for other weapons)"),max_length=250, blank=True, null=True)
    mk_company_involved= models.CharField(_("Murder or killings (Company involved)"),max_length=250, blank=True, null=True)


    what_happened= models.CharField(_("Full description of what happened"),max_length=250, blank=True, null=True)

    reporter_phone= models.CharField(_("Phone number of the reporter"),max_length=250, blank=True, null=True)
    reporter_address= models.CharField(_("Address of the reporter"),max_length=250, blank=True, null=True)
    reporter_email= models.CharField(_("Email of the reporter"),max_length=250, blank=True, null=True)

    # // location
    name_of_area= models.CharField(_("Name of the area"),max_length=250, blank=True, null=True)
    village= models.CharField(_("Name of the village"),max_length=250, blank=True, null=True)
    chief= models.CharField(_("Name of the chief"),max_length=250, blank=True, null=True)
    ward_name= models.CharField(_("Name of the ward"),max_length=250, blank=True, null=True)
    district= models.CharField(_("Name of the district"),max_length=250, blank=True, null=True)
    province= models.CharField(_("Name of the province"),max_length=250, blank=True, null=True)
    location= models.CharField(_("Name of the location"),max_length=250, blank=True, null=True)
    latitude       = models.DecimalField(_("Latitude coordinates"),max_digits=22, decimal_places=16, blank=True, null=True)
    longitude      = models.DecimalField(_("Longitude coordinates"),max_digits=22, decimal_places=16, blank=True, null=True)

    # //Array
    collection_vp = models.JSONField(_("Collection of victims and perpetrators"),default=dict, blank=True, null=True)
    media_files = models.JSONField(_("Collection of the images, videos and audios"),default=dict, blank=True, null=True)

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




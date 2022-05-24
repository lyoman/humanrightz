from statistics import mode
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

VIOLATION_TYPE = (
    ("Forced Displacement", "Forced Displacement"),
    ("Exposure to pollutants", "Exposure to pollutants"),
    ("Loss of land or economic assets", "Loss of land or economic assets"),
    ("Desecration of cultural heritage including graves", "Desecration of cultural heritage including graves"),
    ("Torture and intimidation / harrassment", "Torture and intimidation / harrassment"),
    ("Curtailed freedom of movement", "Curtailed freedom of movement"),
    ("Exposure to degraded environment", "Exposure to degraded environment"),
    ("Limited access to water", "Limited access to water"),
    ("Denied access to social services like Health facilities, School, Markets place", "Denied access to social services like Health facilities, School, Markets place"),
    ("Forced and unpaid labour", "Forced and unpaid labour"),
    ("Child labour", "Child labour"),
    ("Murder / killings", "Murder / killings"),
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
    ("Famale & Male", "Male & Female"),
)

PERPETRATOR_DESCRIPTION = (
    ("Member of Parliament", "Member of Parliament"),
    ("Mining company security guards", "Mining company security guards"),
    ("Artisanal miners ", "Artisanal miners "),
    ("Politician", "Politician"),
    ("Government security agencies (police, army)", "Government security agencies (police, army)"),
    ("Councilors", "Councilors"),
)

MOTIVATIONS_BEHIND = (
    ("Political", "Political"),
    ("To conceal illicit activities and corruption", "To conceal illicit activities and corruption"),
    ("To exercise Power", "To exercise Power"),
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
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE, blank=True, null=True)
    date_reported  = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    company        = models.ForeignKey(CompanyDetail, default=1, on_delete = models.CASCADE, null=True, blank=True)
    type_of_violation      = models.CharField(max_length=250, choices=VIOLATION_TYPE, blank=True, null=True)
    description_of_victims = models.CharField(max_length=250, choices=VICTIMS_DESCRIPTION, blank=True, null=True)
    description_of_perpetrator = models.CharField(max_length=250, choices=PERPETRATOR_DESCRIPTION, blank=True, null=True)
    motivations_behind_incident = models.CharField(max_length=250, choices=MOTIVATIONS_BEHIND, blank=True, null=True)
    what_happened    = models.TextField(blank = True)
    how_it_happened  = models.TextField(blank = True)
    experiment = models.JSONField(default=dict)
    evidence_files   = models.ImageField(upload_to = 'transpired_description/', blank=True, null=True)
    community_description = models.TextField(blank = True)
    location       = models.CharField(max_length=250, blank=True, null=True)
    latitude       = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude      = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    identity_verification = models.FileField(upload_to = 'identity_verification/', blank=True, null=True)
    # file_field     = models.FileField(widget=models.ClearableFileInput(attrs={'multiple': True}))
    active         = models.BooleanField(default=True)
    read_status    = models.BooleanField(default=False)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.type_of_violation

    class Meta:
        ordering = ["-timestamp", "-updated"]


class Victim(models.Model):
    case = models.ForeignKey("report.ReportedCase", related_name="victims", on_delete=models.CASCADE)
    name = models.CharField(_("Victim name"), max_length=200)
    address = models.CharField(_("Victim address"), max_length=200)
    phone =  models.CharField(_("Phone"), max_length=13)

    def __str__(self):
        return self.name




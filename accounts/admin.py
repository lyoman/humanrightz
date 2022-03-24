from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserModelAdmin(UserAdmin):
    list_display 	    = ["id", "username","first_name", "last_name", "email",  "phone_number", "is_active", "is_staff", "is_superuser", "updated", "timestamp"]
    list_display_links  = ["updated", "username"]
    list_editable		= ["is_active"]
    list_filter			= ["is_staff", "is_superuser", "updated", "timestamp", "email", "phone_number"]
    search_fields		= ["username", "email", "phone_number"]
    class Meta:
        model = User
  
admin.site.register(User, UserModelAdmin)
from django.contrib import admin

from apps.admins.forms.users import CustomUserAdmin
from apps.users.models import User


class ModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)

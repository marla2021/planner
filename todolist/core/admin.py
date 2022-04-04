from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name" )
    list_filter = ("is_staff", "is_active", "is_superuser")
    search_fields = ("emailfirst_name", "last_name", "username")
    exclude = ("password", )
    readonly_fields = ["Last login", "Date joined",]


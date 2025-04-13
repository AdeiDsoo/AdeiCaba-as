from django.contrib import admin
from .models import User

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["name", "email", "created_at", "is_active"]
    list_filter=["is_active", "name"]
    ordering=["-created_at"]

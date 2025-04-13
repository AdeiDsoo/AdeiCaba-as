from django.contrib import admin
from .models import User, Course, Branch


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["name", "email", "created_at", "is_active"]
    list_filter=["is_active", "name"]
    ordering=["-created_at"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=["title", "description", "users_qty", "created_at"]
    list_filter=["title", "title"]
    ordering=["-created_at"]

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display=["name", "country", "created_at", "is_active"]
    list_filter=["is_active", "name"]
    ordering=["-created_at"]

from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # columns in the admin list
    search_fields = ("title", "author")                   # search box fields
    list_filter = ("publication_year",)   

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
                   # right-side filter     
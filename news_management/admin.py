from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from news_management.models import Redactor, Topic, Newspaper

admin.site.register(Topic)


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("first_name", "last_name", "years_of_experience")},
        ),
    )


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["title", "topic", "published_date"]
    list_filter = [
        "topic",
    ]
    search_fields = [
        "title",
    ]

from django.contrib import admin

from portfolio.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'logo')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    list_per_page = 10
    readonly_fields = ('created_at', 'modified_at')
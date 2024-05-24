

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from portfolio.models import Project, TypeProject, TypeUrl, TypeTag

admin.site.register(TypeProject)
admin.site.register(TypeUrl)
admin.site.register(TypeTag)

@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    list_display = ('name', 'description', 'logo')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    list_per_page = 10
    readonly_fields = ('created_at', 'modified_at')
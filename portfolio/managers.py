import datetime

from django.db import models
from django.utils.timezone import now


class ProjectManager(models.Manager):
    def get_projects_by_year(self, year=None):
        year = year or now().year
        return self.get_queryset().prefetch_related('tags').filter(created_at__year=year)
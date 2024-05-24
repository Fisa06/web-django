from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from portfolio.models import Project


# Create your views here.

class DetailProjectView(TemplateView):
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = kwargs.get('projekt_id', None)
        try:
            context['project'] = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            context['project'] = None
        return context

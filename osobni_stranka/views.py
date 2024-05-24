from datetime import datetime

from django.db.models import Q
from django.views.generic import TemplateView

from portfolio.models import Project


class BasePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actual_date'] = datetime.now()
        return context

class HomePageView(BasePageView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.get_projects_by_year()

        return context


class AboutPageView(BasePageView):
    template_name = 'about.html'
from datetime import datetime

from django.views.generic import TemplateView

class BasePageView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actual_date'] = datetime.now()
        return context

class HomePageView(BasePageView):
    template_name = 'home.html'


class AboutPageView(BasePageView):
    template_name = 'about.html'
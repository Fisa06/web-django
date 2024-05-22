from datetime import datetime

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actual_date'] = datetime.now()
        print(context)
        return context
class AboutPageView(TemplateView):
    template_name = 'about.html'
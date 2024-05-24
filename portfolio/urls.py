from django.urls import path

from portfolio.views import DetailProjectView

urlpatterns = [
    path('detail/<int:projekt_id>', DetailProjectView.as_view(), name='detail_project'),
]
from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

from .views import FileDetailView

urlpatterns = [
    url(r'^file/(?P<pk>\d+)/$', FileDetailView.as_view(), name='file'),
]

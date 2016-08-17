from StringIO import StringIO

from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import DetailView
from django.conf import settings

from .models import File


class FileDetailView(DetailView):
    model = File

    def get(self, *args, **kwargs):
        self.obj = self.get_object()
        response = HttpResponse()
        response['mimetype'] = 'text/plain'
        response['Content-Disposition'] = 'attachment; filename="%s"' % self.obj.pk
        response.write(self.obj.upload)
        return response
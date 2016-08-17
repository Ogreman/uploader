from django.contrib import admin
from .models import File
from .forms import FileForm


@admin.register(File)
class FileAdmin(admin.ModelAdmin):

    def length(self, obj):
        return len(obj.upload)

    def change_view(self, request, obj=None):
        from django.core.urlresolvers import reverse
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(File.objects.get(pk=obj).get_absolute_url())

    form = FileForm
    list_display = ('__str__', 'length')
    view_on_site = True

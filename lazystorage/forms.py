from django import forms

from .models import File

class FileForm(forms.ModelForm):
    new_file = forms.FileField()

    class Meta:
        model = File
        fields = ('new_file', )

    def save(self, commit=True):
        contents = self.cleaned_data['new_file'].read()
        self.instance.upload = contents
        return super(FileForm, self).save(commit)

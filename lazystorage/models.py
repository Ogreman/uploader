from django.core.urlresolvers import reverse
from django.db import models


class File(models.Model):
    
    upload = models.BinaryField()

    def __str__(self):
        return '[file]: %s' % self.pk

    class Meta:
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('file', kwargs={'pk': self.pk})

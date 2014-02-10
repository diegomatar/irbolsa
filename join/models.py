from django.db import models
from django.utils.encoding import smart_unicode

class Join(models.Model):
    email = models.EmailField(max_length=250)
    nome = models.CharField(max_length=250, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    
    def __unicode__(self):
        return smart_unicode(self.email)

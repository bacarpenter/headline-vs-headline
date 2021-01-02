from django.db import models

# Create your models here.
class HeadlineListing(models.Model):
    headline_text = models.CharField(max_length=500)
    accessed = models.DateTimeField()
    source_url = models.CharField(max_length=200)
    author = models.CharField(default="", max_length=200)
    source = models.CharField(max_length=200)

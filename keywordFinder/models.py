from django.db import models


class Url_Keyword(models.Model):
    url = models.TextField(default='')
    created = models.DateTimeField(auto_now=True)
    keywords = models.TextField()

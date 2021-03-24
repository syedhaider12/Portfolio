from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=30)
    emial = models.EmailField(max_length = 254)
    subject = models.CharField(max_length=50)
    textarea = models.TextField()


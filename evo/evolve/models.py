from django.db import models


# Create your models here.
class Doc(models.Model):
    document = models.FileField()

    def __str__(self):
        return str(self.document) 
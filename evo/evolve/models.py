from django.db import models


# Create your models here.
class Doc(models.Model):
    document = models.FileField()

    def __str__(self):
        return str(self.document) 


#admin upload
class FilesAdmin(models.Model):
    up = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title
    
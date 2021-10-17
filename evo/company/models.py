from os import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class JobPlan(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    customer = models.CharField(max_length=200)
    file_no = models.CharField(max_length=200)
    origin_port = models.CharField(max_length=200)
    destination_port = models.CharField(max_length=200)
    description = models.TextField()
    product = models.CharField(max_length=200)
    forwarder = models.CharField(max_length=200)
    clearing_agent = models.CharField(max_length=200)
    marketer = models.CharField(max_length=200)
    buying = models.CharField(max_length=200)
    selling = models.CharField(max_length=200)
    margin = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
    

    def get_absolute_url(self):
        return reverse('job_p_detail', kwargs={'pk': self.pk})


class MarketPlan(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    file_ref_no = models.CharField(max_length=200)
    account_code_no = models.CharField(max_length=200)
    marketer = models.CharField(max_length=200)
    director_name = models.CharField(max_length=200)
    director_no = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    product_description = models.TextField()
    comodity = models.CharField(max_length=200)
    communication = models.CharField(max_length=200)
    travelling_accomodation = models.CharField(max_length=200)
    advertising = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
    remarks = models.TextField()


    def __str__(self):
        return str(self.name)


    def get_absolute_url(self):
        return reverse('market_p_detail', kwargs={'pk': self.pk})

    



from django.db import models
from django.forms import fields
from .models import JobPlan, MarketPlan
from django import forms

class JobForm(forms.ModelForm):
    class Meta:
        model = JobPlan
        fields = '__all__'


class MarketPlanForm(forms.ModelForm):
    class Meta:
        model = MarketPlan
        fields = '__all__'


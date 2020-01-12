from django.db import models
from datetime import datetime
from django.urls import reverse
from django.conf import settings

# Create your models here.


class CallAllocation(models.Model):


    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    

    hub_status = (
        ('not_yet', 'NotYet',),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On hold'),
        ('completed', 'Completed'),

    )
    
    name = models.CharField(max_length=200,blank=True)
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )
    product = models.CharField(max_length=200)
    s_no = models.IntegerField(blank=True, null=True)
    issue = models.CharField(max_length=200)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES)
    estimate_hours = models.FloatField()
    engineer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    status = models.CharField(max_length=15,choices=hub_status,blank=False,null=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    remarks = models.TextField( max_length=2000,blank=True,null=True)

    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    end_time = models.TimeField(blank=True,null=True)
    
    
    def __str__(self):
        return self.engineer.username

    def get_absolute_url(self):
        return reverse('dashboard')
    

    

class Customer(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name







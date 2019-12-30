from django.db import models
from datetime import datetime

# Create your models here.



class CallAllocation(models.Model):


    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )
    

    hub_status = (
        ('not_yet', 'Not Yet'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On hold'),
        ('completed', 'Completed'),

    )
    
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
    )
    product = models.CharField(max_length=200)
    s_no = models.IntegerField()
    issue = models.CharField(max_length=200)
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES)
    estimate_hours = models.FloatField()
    engineer = models.ForeignKey(
        'Engineer',
        on_delete=models.CASCADE,
    )

    status = models.CharField(max_length=15,choices=hub_status)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField()
    remarks = models.CharField( max_length=2000)


    def __str__(self):
        return self.engineer
 

class Customer(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Engineer(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name





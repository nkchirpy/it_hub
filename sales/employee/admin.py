from django.contrib import admin
from .models import CallAllocation, Customer, Engineer

# Register your models here.


admin.site.register(CallAllocation)
admin.site.register(Customer)
admin.site.register(Engineer)
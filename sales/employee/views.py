from django.shortcuts import render
from django.views.generic import TemplateView,CreateView


# Create your views here.


class Callview(TemplateView):
    template_name = 'employee/call.html'


class Engineerview(TemplateView):
    template_name = 'employee/engineer.html'

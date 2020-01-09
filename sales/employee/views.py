from django.shortcuts import render
from django.views.generic import TemplateView,CreateView

# from django.views.generic.edit import CreateView

from .models import CallAllocation
from .forms import ItCallAllocation
# Create your views here.


def to_do_list(request):

    if request.user.is_superuser:
        tasks = CallAllocation.objects.all()

    else:
        tasks = CallAllocation.objects.filter(engineer=request.user)
    
    return render(request, 'employee/engineer.html', {'tasks': tasks})


class CallView(CreateView):
    model = CallAllocation
    form_class = ItCallAllocation
    template_name = 'employee/callallocation_form.html'
    # fields = ['customer','product','issue','priority','estimate_hours','engineer','status','start_date','end_date','remarks']





class Engineerview(TemplateView):
    template_name = 'employee/engineer.html'


class Dashboard(TemplateView):
    template_name = 'employee/dashboard.html'

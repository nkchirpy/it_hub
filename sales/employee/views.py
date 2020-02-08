from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,CreateView

from .models import CallAllocation
from .forms import ItCallAllocation
from datetime import datetime
# Create your views here.


def todo_edit(request, pk):

    
    post = get_object_or_404(CallAllocation, pk=pk)
    if request.method == "POST":
        form = ItCallAllocation(request.POST, instance=post)
        
        
        if form.is_valid():
            post = form.save(commit=False)


            get_column = request.POST['actual_time']

            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            end_date = form.cleaned_data['end_date']
            end_time = form.cleaned_data['end_time']
            dt_object1 = datetime.strptime(str(start_date) + ' ' + str(start_time), "%Y-%m-%d %H:%M:%S")
            dt_object2 = datetime.strptime(str(end_date) + ' ' + str(end_time), "%Y-%m-%d %H:%M:%S")
            actual = dt_object2 - dt_object1
            post.actual_time = actual

            
            post.save()
            return redirect('dashboard')
    else:
        
        form = ItCallAllocation(instance=post)
    return render(request, 'employee/callallocation_update_form.html', {'form': form})

def to_do_list(request):

    
    if request.user.is_authenticated:

        if request.user.is_superuser:
            
            tasks = CallAllocation.objects.filter(status__in=('Not-Yet','In-Progress','On-Hold'))
            return render(request, 'employee/engineer.html', {'tasks': tasks})

        else:
            tasks = CallAllocation.objects.filter(engineer=request.user, status__in=('Not-Yet','In-Progress','On-Hold'))
            return render(request, 'employee/engineer.html', {'tasks': tasks})
    
    else:

        return render(request, 'employee/hub_base.html')


def done(request):

    
    if request.user.is_authenticated:

        if request.user.is_superuser:
            
            tasks = CallAllocation.objects.filter(status='Completed')
            return render(request, 'employee/done_engineer.html', {'tasks': tasks})

        else:
            tasks = CallAllocation.objects.filter(engineer=request.user, status='Completed')
            return render(request, 'employee/done_engineer.html', {'tasks': tasks})
    
    else:

        return render(request, 'employee/hub_base.html')


def done_view(request, pk):

    
    post = get_object_or_404(CallAllocation, pk=pk)
    if request.method == "POST":
        form = ItCallAllocation(request.POST, instance=post)
       
    else:
        
        form = ItCallAllocation(instance=post)
    return render(request, 'employee/callallocation_view_form.html', {'form': form})




class CallView(CreateView):
    model = CallAllocation
    form_class = ItCallAllocation
    template_name = 'employee/callallocation_form.html'


class Dashboard(TemplateView):
    template_name = 'employee/dashboard.html'




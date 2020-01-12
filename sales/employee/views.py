from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,CreateView

from .models import CallAllocation
from .forms import ItCallAllocation
# Create your views here.


def todo_edit(request, pk):

    print("--======",)
    post = get_object_or_404(CallAllocation, pk=pk)
    if request.method == "POST":
        form = ItCallAllocation(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('dashboard')
    else:
        
        form = ItCallAllocation(instance=post)
        # print("-=-=-=-=-=-",form)
    return render(request, 'employee/callallocation_update_form.html', {'form': form})

def to_do_list(request):

    
    if request.user.is_authenticated:
        print('come on---am i triggering---')

        if request.user.is_superuser:
            tasks = CallAllocation.objects.all()
            return render(request, 'employee/engineer.html', {'tasks': tasks})

        else:
            tasks = CallAllocation.objects.filter(engineer=request.user)
            return render(request, 'employee/engineer.html', {'tasks': tasks})
    
    else:

        return render(request, 'employee/hub_base.html')


class CallView(CreateView):
    model = CallAllocation
    form_class = ItCallAllocation
    template_name = 'employee/callallocation_form.html'


class Dashboard(TemplateView):
    template_name = 'employee/dashboard.html'




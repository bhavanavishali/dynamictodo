from django.shortcuts import render
from .models import Tasks
from django.views.generic import ListView

# Create your views here.
def index(request):
    task1 =Tasks.objects.all()
    if request.method=='POST':
        task= request.POST.get('task')
        priority = request.POST.get('priority')
        data = Tasks(task=task,priority=priority)
        data.save()
    return render(request,'index.html',{'task1':task1})

class Taskview(ListView):
    model = Tasks
    template_name = 'index.html'
    context_object_name = 'task1'
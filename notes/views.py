from django.shortcuts import render,redirect
from .models import Notes
# Create your views here.
def task_list(request):
    tasks=Notes.objects.all()
    return render(request,'notes/task_list.html',{'tasks':tasks})
def add_task(request):
    if request.method=='POST':
        title=request.POST['name']
        description=request.POST['description']
        task=Notes(title=title,description=description)
        task.save()
        return redirect('task_list')    
    return render(request,'notes/add_task.html')

def delete_task(request,id):
    task=Notes.objects.get(id=id)
    task.delete()
    # redirect back to the task_list view after deleting a task
    # this will reload the page with the updated list of task
    return redirect('task_list')
from django.shortcuts import redirect, render, HttpResponse
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    context = {
        'tasks':tasks,
        'form':form,
    }
    return render(request, 'index.html', context)

@require_POST
def addTask(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_task = Todo(task = request.POST['task'])
        new_task.save()

    return redirect('home')

def completeTask(request, pk):
    task = Todo.objects.get(id = pk)
    task.complete = True
    task.save()

    return redirect('home')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('home')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact = True).delete()

    return redirect('home')

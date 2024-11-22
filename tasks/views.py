from django.shortcuts import render , redirect
from django.template.loader import get_template
from .models import *




# Create your views here.

def task_list(request):
   tasks = task.objects.all()
   context= {'task':tasks}

   # Debug print
   print(get_template('task.html').origin)
   return render(request , 'task.html' , context)

def add_task(request):
   if request.method =="POST":
      title= request.POST.get('title')
      task.objects.create(title=title)
      return redirect('/task_list/')
   return render(request , 'add_task.html')
   

def delete_task(request, task_id):
   tasks=task.objects.get(id=task_id)
   tasks.delete()
   return redirect('/task_list/')

def toggle_task(request , task_id):
   tasks=task.objects.get(id=task_id)
   print(f"tasks{task_id} - Before toggle: {task.completed}")
   tasks.completed= not task.completed
   tasks.save()
   print(f"tasks{task_id} - After toggle: {task.completed}")
   return redirect('/task_list/')


      

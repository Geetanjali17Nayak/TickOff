from django.shortcuts import render , redirect
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
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

def login_page(request):
   if request.method =="POST":
      username=request.POST.get('username')
      password = request.POST.get('password')

      if not User.Objects.filter(username=username).exists():
          messages.error(request, "Invalid Username")
          return redirect('/login_page/')
      
      user= authenticate(username=username , password=password)

      if user is None:
         messages.error(request , "Invalid Password")
         return redirect('/login_page/')
      else:
         login(request , user)
         return redirect ('/task_list/')
      
   return render(request , 'login.html')  

def logout(request):
   logout(request)
   return redirect('/login_page/')

def register_page(request):
   if request.method=="POST":
      first_name= request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')

      user= User.objects.filter(username=username)

      if user.exists():
         messages.info(request , "Username already taken")
         return redirect('/register_page/')
      
      user = User.objects.create(
         first_name=first_name,
         last_name = last_name ,
         username=username
      )

      user.set_password(password)
      user.save()

      messages.success(request , "Account created Successfully")
      return redirect('/register_page/')
   return render(request , 'task.html')
   




      

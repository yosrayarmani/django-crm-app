from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm 
from .models import Record

#home page 
def home(request):
  records = Record.objects.all() # .all >> grab all the abjects from the table
  #-------------if a user is POSTING-------------
  #check if logging in
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request,user)
      messages.success(request, "Logged In Successfully!")
      #redirect to home page
      return redirect('home')
    else:
      messages.success(request,"Username or Password is incorrect, Please Try Again!")
      return redirect('home')
  #-------------if a user is POSTING-------------
      
  #-------------else (they're not posting)->> they're 'GETTING' >> then we can show the home page-------------
  else:
    return render(request, 'home.html', {'records':records}) #in home.html << {% if records %}

#function should be named logout_user so it won't conflict with the function logout that we imported from django.contrib
def logout_user(request):
  logout(request)
  messages.success(request, "You Have Been Logged Out...")
  return redirect('home')

def register_user(request):
  # whenever they filled the form send to SignUpForm 
  if request.method == 'POST': #IF user is filling and posting the form
    form = SignUpForm(request.POST)
    if form.is_valid(): 
      #save the data into variables
      form.save()
      # authenticate and login
      username = form.cleaned_data['username'] 
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password) 
      login(request, user)
      messages.success(request,"Account Created!")
      return redirect('home')
  else: #ELSE user is not posting the form and just going to the website >> user want to fill the form but have not done it yet 
    form = SignUpForm() #don't have to pass in the POST request
    return render(request, 'register.html', {'form':form}) #pass the form into register.html page  
  return render(request, 'register.html', {'form':form})


def customer_record(request, pk): #pk:primary key of a record
  if request.user.is_authenticated:
    #look for the record
    costumer_record = Record.objects.get(id=pk) # .get >> when we want specific aboject
    #id is from 'migrations<0001_initial.py'
    return render(request, 'record.html', {'costumer_record':costumer_record}) # go to 'record.html' and pass 'costumer_record'
  else:
    messages.success(request, "You must be logged in first!")
    return redirect('home')
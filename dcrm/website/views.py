from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm 
# Create your views here.
#create the home page 
def home(request):
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
      
  #-------------else (they're not posting)->> they're GETTING then we can show the home page-------------
  else:
    return render(request, 'home.html', {})

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
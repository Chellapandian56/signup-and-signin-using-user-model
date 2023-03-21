from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    return render (request,"userapp/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["Email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        user = User.objects.create(username=username,email=email,password=pass1)
        user.fname = fname
        user.lname = lname

        user.save()
        messages.success(request,"Registered successfully")
        return redirect("signin")
    return render (request,"userapp/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        Pass1 = request.POST['pass1']

        login_user = authenticate(username = username,password=Pass1)
        if login_user is not None:
            login(request,login_user)
            fname = login_user.first_name
            return render(request,"userapp/index.html",{"fname":fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect("home")
    return render(request,"userapp/signin.html")

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return HttpResponse("This is home page")

def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cf=request.POST.get('confirm-password')
        my_user=User.objects.create_user(username,email,password)
        my_user.save()
        return HttpResponse("user is succesfully saved")
        return redirect('login')

        
    return render(request, 'signup.html') 
def loginpage(request):
    if request.method=='POST':
        us=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=us,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("User name and password is incorrect")
    return render(request, 'login.html')

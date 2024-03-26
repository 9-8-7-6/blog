from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"the email is already used!")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"the username is already used!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid account!')
            return redirect('login')
    else:
        return render(request,'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
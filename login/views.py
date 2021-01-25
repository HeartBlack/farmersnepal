from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import logout
from django.contrib import messages
from .decoretors  import login_excluded
# Create your views here.




@login_excluded('home')
def login(request):
    
     
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials not matched')
            return redirect('login')
    else:
        return render(request,'login.html')



    


@login_excluded('home')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('/register')    
            else:    
                user = User.objects.create_user(username=username, email=email,password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request,'Password did not matched.')
            return redirect('/register')
    else:
        return render(request,'register.html')

     



def logout(request):
    auth.logout(request)
    return redirect('home')
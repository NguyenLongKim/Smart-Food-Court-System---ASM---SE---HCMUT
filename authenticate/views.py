from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

def GetLogin(request):
    return render(request, 'login/index.html')

def PostLogin(request):
    inusrname = request.POST.get('username')
    inpassword = request.POST.get('password')
    myuser = authenticate(username=inusrname, password=inpassword)
    if ( (myuser != None) and (myuser.type_account=='customer') ):
        login(request, myuser)
        return redirect('customer:view-menu')
    else:
        return HttpResponse('Login failed')

def LogOut(request):
    logout(request)
    return redirect('authenticate:get_login')
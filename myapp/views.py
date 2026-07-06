from django.shortcuts import render
from .models import datas,user
# Create your views here.
def home(request):
    products=datas.objects.all()
    return render(request,'home.html',{'pro':products})
def login(request):
    if request.method=="POST":
        action=request.POST.get("action")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if action=="save":
            user.objects.create(user_email=email,user_password=password)
        else:
            return render(request,'forgetpwd.html')

    
    return render(request,'login.html')
def downloads(request):
    return render(request,'home.html')

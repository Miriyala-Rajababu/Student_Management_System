from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q





'''
from .models import std_model
from .models import std_result

def std_reg(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['password']
        confrompassword=request.POST['confrompassword']
        if confrompassword==password:
            obj=std_model(Name=name,Email=email,Number=number,Password=password)
            obj.save()
            return redirect('/std_login')

        else:
            return HttpResponse("password and conform must be same")
    
    

    return render(request,"Registration.html")


def std_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Filter the user based on the provided email and password
        user = std_model.objects.filter(Email=email, Password=password).first()

        if user:
            # Use the Django login function correctly with the request and user object
            return redirect('/home')
        else:
            return HttpResponse("Invalid email or password.")
            
    return render(request, "Login.html")


def std_logout(request):   
    logout(request)
    return redirect('/std_login')


def get_data(request):
    data=std_result.objects.all()

    return render(request,"Student_result.html",{"show":data})


def std_home(request):
    return render(request,"Home.html")
def std_fee(request):
    return render(request,"Fee.html")



def get_id(request):
    idvalues = None
    if request.method == "POST":
        myid = request.POST.get('search')
        if myid.isdigit():
            idvalues = std_result.objects.get(id=myid)
        elif myid.isalpha():
            idvalues = std_result.objects.get(Name=myid)
        else:
            return HttpResponse("NOt valid")
     
            
    return render(request, "Student_result.html", {"show": [idvalues] if idvalues else []})



def std_add(request):
    if request.method=='POST':
        name=request.POST['name']
        cource=request.POST['cource']
        hallticket=request.POST['hallticket']
        result=request.POST['result']
    
        obj=std_result(Name=name,Cource=cource,Hallticket=hallticket,result=result)
        obj.save()
        return redirect('/get_data')

    return render(request,"Addnew.html")





def std_att(request):
    return render(request,"Attendence.html")












''''''def login_page(request):
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['password']
        user=authenticate(request,username=a,password=b)

        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully logged in!')
            return redirect("/get")
        else:
             return redirect("/login")
    return render(request,"login.html")'''

from .models import Ticket

def tic(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        obj = Ticket(name=n, email=e)
        obj.save()
        return redirect('')  # Redirect to home or any other route

    return render(request, "cu.html")








def clint(request):
    obj = Ticket.objects.order_by('-id').first()  # Fetch the latest ticket by id

    return render(request, "clint.html", {'ticket': obj})




def display_max_ticket(request):
    
    max_ticket = Ticket.objects.order_by('-id').first() 
    

    return render(request, "gettic.html", {'ticket': max_ticket})






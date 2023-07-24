from django.shortcuts import render , redirect
from .models import Student
# from django.http import response


# Create your views here.

def home(request):
    stud = Student.objects.all()
    return render(request , 'index.html',{'stud':stud})

def add_stu(request):
    if request.method=='POST':
        stu_roll = request.POST.get('roll')
        stu_name = request.POST.get('name')
        stu_email = request.POST.get('email')
        stu_address = request.POST.get('address')
        stu_phone = request.POST.get('phone')
        
        stud = Student()
        stud.roll = stu_roll
        stud.name = stu_name
        stud.email = stu_email
        stud.address = stu_address
        stud.phone = stu_phone
        stud.save()
        return redirect("home")
    return render (request,'add-stu.html')

def delete_std(request , roll):
    s = Student.objects.get(pk=roll)
    s.delete()
    return redirect("/")

def update_std(request , roll):
    stud = Student.objects.get(pk=roll)
    return render(request ,"update.html",{"stud":stud})

def do_update_std(request , roll):
        stu_roll = request.POST.get("roll")
        stu_name = request.POST.get("name")
        stu_email = request.POST.get("email")
        stu_address = request.POST.get("address")
        stu_phone = request.POST.get("phone")
    
        stud = Student.objects.get(pk=roll)
        
        stud.roll =stu_roll
        stud.name =stu_name
        stud.email =stu_email
        stud.address =stu_address
        stud.phone =stu_phone
        stud.save()
        return redirect("/")


    



    



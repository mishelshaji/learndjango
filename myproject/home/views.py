from django.shortcuts import render, HttpResponse, redirect
from .forms import NewEmployeeForm
from .models import Employees

# Create your views here.
def home(request):
    if request.method == "GET":
        nef = NewEmployeeForm()
        return render(request, 'index.html', {'data': nef})
    
    else:
        nef = NewEmployeeForm(request.POST)
        if nef.is_valid():
            nef.save()
            return HttpResponse("Data saved")
        else:
            return render(request, 'index.html', {'data': nef})

def about(request):
    return render(request, 'about.html')

def viewdata(request):
    emps = Employees.objects.all()
    # emps = Employees.objects.filter(name__startswith='u')[:1]
    # emps = Employees.objects.get(age=500)
    return render(request, 'viewdata.html', {'data': emps})

def addhtmldata(request):
    if request.method == "GET":
        return render(request, 'htmlform.html')

    else:
        emp = Employees()
        emp.name = request.POST.get('name')
        emp.emp_age = request.POST.get('age')
        emp.department = request.POST.get('department')
        emp.save()
        return redirect('viewdata')
    
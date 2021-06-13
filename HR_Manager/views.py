from django.shortcuts import render,redirect
from Employee.models import Employee,Department
from django.contrib import messages
# Create your views here.
def index(request):
    emp=Employee.objects.all()
    return render(request,'index.html',{'Employees':emp})

def addView(request):
    dep=Department.objects.all()
    print('In AddView')
    return render(request,'addView.html',{'department':dep})

def storeEmployee(request):
    try:
        emp=Employee()
        dep=Department()
        dep.name=request.POST.get('department')
        
        emp.name=request.POST.get('emp_name')
        emp.email=request.POST.get('emp_email')
        emp.cnic=request.POST.get('cnic')
        emp.department=dep
        
        image = request.FILES['image'] 
        emp.image.save(image.name,image,)
        
        emp.save()
        
        messages.success(request, "Employee Added Successfully")
        return redirect('/')
    except:
        return render(request,'error.html')

def Delete(request,cnic):
    emp=Employee.objects.get(cnic=cnic)
    emp.delete()
    messages.success(request, "Employee Deleted Successfully")
    return redirect('/')

def showUpdate(request,cnic):
    emp=Employee.objects.get(cnic=cnic)
    dep=Department.objects.all()
    return render(request,'update.html',{'Employee':emp,'Departments':dep})

def update(request,cnic):
    try:
        dep=Department()
        dep.name=request.POST.get('department')
        
        Employee.objects.filter(cnic=cnic).update(cnic=request.POST.get('cnic'))
        
        emp=Employee.objects.get(cnic=request.POST.get('cnic'))
        emp.name=request.POST.get('emp_name')
        emp.email=request.POST.get('emp_email')
        # emp.cnic=request.POST.get('cnic')
        emp.department=dep
        
        try:
            image = request.FILES['image'] 
            emp.image.save(image.name,image,)
        except:
            pass
            
        emp.save()
        
        messages.success(request, "Employee Updated Successfully")
        return redirect('/')
    except:
        return render(request, 'error.html')

def open(request,cnic):
    emp=Employee.objects.get(cnic=cnic)
    return render(request,'open.html',{'Employee':emp})
    
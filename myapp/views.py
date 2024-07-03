from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.models import Employee

from myapp.forms import EmpForm

# Create your views here.

class EmployeeListView(View):
    
    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"emp_list.html",{"data":qs})

class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmpForm()

        return render(request,"emp_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=EmpForm(request.POST)
        
        if form_instance.is_valid():

            data=form_instance.cleaned_data

            # print(data)

            Employee.objects.create(**data)

            return redirect("emp-list")

        else:

            return render(request,"emp_add.html",{"form":form_instance})

class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,"emp_detail.html",{"data":qs})

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        
        Employee.objects.get(id=id).delete()

        return redirect("emp-list")
        

class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_object=Employee.objects.get(id=id)

        dictionary={
            "Name":employee_object.name,
            "salary":employee_object.salary,
            "department":employee_object.department,
            "location":employee_object.location,
            "address":employee_object.address
        }

        form_instance=EmpForm(initial=dictionary)

        return render(request,"emp_edit.html",{"form":form_instance})


    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        form_instance=EmpForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)

            return redirect("emp-list")

        else:

            return render(request,"emp_edit.html",{"form":form_instance})
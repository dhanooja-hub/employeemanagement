from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from myapp.models import Employee

from api.serializers import EmployeeSerializer

# Create your views here.

class EmployeeListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        serializer_instance=EmployeeSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        

        serializer_instance=EmployeeSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        



        
    
class EmployeeRetrieveUpdateDeleteView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_obj=Employee.objects.get(id=id)

        serializer_instance=EmployeeSerializer(employee_obj,many=False)

        return Response(data=serializer_instance.data)

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_obj=Employee.objects.get(id=id)

        serializer_instance=EmployeeSerializer(data=request.data,instance=employee_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)

        

    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return Response(data={"message":"employee deleted"}) 

class DepartmentView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all().values_list("department",flat=True).distinct()

        return Response(data=qs)
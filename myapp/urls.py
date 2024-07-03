from django.urls import path
from myapp import views

urlpatterns = [
    

    path('employee/all/',views.EmployeeListView.as_view(),name="emp-list"),

    path('emp/add/',views.EmployeeCreateView.as_view(),name="emp-create"),
    
    path('emp/<int:pk>/',views.EmployeeDetailView.as_view(),name="emp-detail"),

    path('emp/<int:pk>/delete',views.EmployeeDeleteView.as_view(),name="emp-remove"),

    path('emp/<int:pk>/edit',views.EmployeeUpdateView.as_view(),name="emp-edit")
]
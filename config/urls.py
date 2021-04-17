"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from MedicApp import views

router = routers.DefaultRouter()
router.register("company", views.CompanyViewSet, basename="company")
router.register("companybank", views.CompanyBankViewset,
                basename="companybank")
router.register("medicine", views.MedicineViewset, basename="medicine")
router.register("employee", views.EmployeeViewset, basename="employee")
router.register("customer", views.CustomerViewset, basename="customer")
router.register("bill", views.BillViewset, basename="bill")
router.register("customerrequest", views.CustomerRequestViewset,
                basename="customerrequest")
router.register("companyaccount", views.CompanyAccountViewset,
                basename="companyaccount")
router.register("employee_all_bank", views.EmployeeBankViewset,
                basename="employee_all_bank")
router.register("employee_all_salary", views.EmployeeSalaryViewset,
                basename="employee_all_salary")
# router.register("employee_bank_by_id", views.EmployeeSalaryViewset,
#                 basename="employee_bank_by_id")
# router.register("employee_salary_by_id", views.EmployeeSalaryViewset,
#                 basename="employee_salary_by_id")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api/companybyname/<str:name>',
         views.CompanyNameViewSet.as_view(), name="companybyname"),
    path('api/companyonly/', views.CompanyOnlyViewSet.as_view(), name="companyonly"),
    # path('api/employee_bank_by_id/<str:employee_id>',
    #      views.EmployeeBankByEIDViewSet.as_view({'get': 'retrieve'}), name="employee_bank_by_id"),
    # path('api/employee_salary_by_id/<str:employee_id>',
    #      views.EmployeeSalaryByEIDViewSet.as_view({'get': 'retrieve'}), name="employee_salary_by_id"),


]

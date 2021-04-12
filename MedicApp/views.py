from rest_framework import generics
from rest_framework.serializers import Serializer
from MedicApp import serializes
from MedicApp.serializes import BillSerializer, CompanyBankSerializer, CompanySerializer, CustomerRequestSerializer, CustomerSerializer, EmployeeSerializer, MedicalDetailsSerializer, MedicalDetailsSerializerSimple, MedicineSerializer
from MedicApp.models import Bill, Company, CompanyBank, Customer, CustomerRequest, Employee, MedicalDetails, Medicine
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(
            company, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Company Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Company Data"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(
                company, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {
                "error": False, "message": "Company Data Updated Successfully."}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Update Company Data"}
        return Response(dict_response)


class CompanyBankViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Company Bank Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Company Bank Data"}
        return Response(dict_response)

    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(
            companybank, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(
            companybank, context={"request": "request"})
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(
            companybank, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class MedicineViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = MedicineSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # access id that was just saved to db
            medicine_id = serializer.data['id']

            medicine_details_list = []
            for medicine_detail in request.data["medicine_details"]:
                medicine_detail["medicine_id"] = medicine_id
                medicine_details_list.append(medicine_detail)

            serializer2 = MedicalDetailsSerializer(
                data=medicine_details_list, many=True, context={"request": request})
            serializer2.is_valid()
            serializer2.save()

            dict_response = {"error": False,
                             "message": "Medicine Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Medicine Data"}
        return Response(dict_response)

    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(
            medicine, many=True, context={"request": request})

        medicine_data = serializer.data()
        new_medicine_list = []

        for medicine in medicine_data:
            medicine_details = MedicalDetails.objects.filter(
                medicine_id=medicine["id"])
            medicine_details_serializer = MedicalDetailsSerializerSimple(
                medicine_details, many=True)
            medicine["medicine_details"] = medicine_details_serializer.data
            new_medicine_list.append(medicine)

        response_dict = {
            "error": False, "message": "All Medicine List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(
            medicine, context={"request": "request"})

        serializer_data = serializer.data
        medicine_details = MedicalDetails.objects.filter(medicine_id=serializer_data["id"])
        medicine_details_serializer = MedicalDetailsSerializerSimple(medicine_details, many=True)
        serializer_data["medicine_details"] = medicine_details_serializer.data
       

        
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Medicine.objects.all()
        medicine = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(
            medicine, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class EmployeeViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = EmployeeSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Employee Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Employee Data"}
        return Response(dict_response)

    def list(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(
            employee, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Employee List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = EmployeeSerializer(
            employee, context={"request": "request"})
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Employee.objects.all()
        employee = get_object_or_404(queryset, pk=pk)
        serializer = MedicineSerializer(
            employee, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class CustomerViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CustomerSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Customer Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Customer Data"}
        return Response(dict_response)

    def list(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializer(
            customer, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Customer List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(
            customer, context={"request": "request"})
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(
            customer, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class BillViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = BillSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Bill Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Bill Data"}
        return Response(dict_response)

    def list(self, request):
        bill = Bill.objects.all()
        serializer = CustomerSerializer(
            bill, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Bill List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = Bill.objects.all()
        bill = get_object_or_404(queryset, pk=pk)
        serializer = BillSerializer(
            bill, context={"request": "request"})
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = Bill.objects.all()
        bill = get_object_or_404(queryset, pk=pk)
        serializer = BillSerializer(
            bill, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class CustomerRequestViewset(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CustomerSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False,
                             "message": "Request Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Request Data"}
        return Response(dict_response)

    def list(self, request):
        customer_request = CustomerRequest.objects.all()
        serializer = CustomerRequestSerializer(
            customer_request, many=True, context={"request": request})
        response_dict = {
            "error": False, "message": "All Request List Data", "data": serializer.data}
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        queryset = CustomerRequest.objects.all()
        customer_request = get_object_or_404(queryset, pk=pk)
        serializer = CustomerRequestSerializer(
            customer_request, context={"request": "request"})
        return Response({"error": False, "message": "single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        queryset = CustomerRequest.objects.all()
        customer_request = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(
            customer_request, data=request.data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response({"error": False, "message": "Update Successful"})


class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Company.objects.filter(name=name)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})

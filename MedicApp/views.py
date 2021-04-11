from MedicApp import serializes
from MedicApp.serializes import CompanySerializer
from MedicApp.models import Company
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
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
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False,
                             "message": "Company Data Save Successful"}
        except:
            dict_response = {
                "error": True, "message": "Error While Trying to Save Company Data"}
        return Response(dict_response)


company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})

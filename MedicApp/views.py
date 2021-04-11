from MedicApp.serializes import CompanySerializer
from MedicApp.models import Company
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
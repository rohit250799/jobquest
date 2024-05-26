from django.shortcuts import render
from rest_framework import generics, status, viewsets
from .models import Job
from .serializers import JobSerializer

# Create your views here.

class JobsList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
# from django.shortcuts import render
from rest_framework import generics
from .serializer import BreedSerializer
from .models import Breeds

class BreedList(generics.ListCreateAPIView):
  queryset = Breeds.objects.all()
  serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Breeds.objects.all()
  serializer_class = BreedSerializer






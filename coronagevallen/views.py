from django.shortcuts import render
from rest_framework import viewsets
from .models import Coronagevallen
from .serializers import coronaSerializer

class CoronaView(viewsets.ModelViewSet):
    queryset = Coronagevallen.objects.all()
    serializer_class = coronaSerializer
# Create your views here.


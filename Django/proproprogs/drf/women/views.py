from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import WomenSerializer
from .models import Women

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Angelina Jolie'})
    
    def post(self, request):
        return Response({'title': 'Jenifer Shrader Lawrence'})
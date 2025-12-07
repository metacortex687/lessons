from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import WomenSerializer
from .models import Women, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminUser,)

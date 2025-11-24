from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import WomenSerializer
from .models import Women

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts': list(lst)})
    
    def post(self, request):
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})
    
    def delete(self, request):
        woman = get_object_or_404(Women, id=request.data['id'])
        woman.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
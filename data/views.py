from .serializers import *
from rest_framework import generics
from .models import *

class GetCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter()
    lookup_field = 'slug'


class GetModels(generics.ListAPIView):
    serializer_class = ModelSerializer
    queryset = Model.objects.all()

class GetModel(generics.RetrieveAPIView):
    serializer_class = ModelSerializer
    queryset = Model.objects.filter()
    lookup_field = 'slug'
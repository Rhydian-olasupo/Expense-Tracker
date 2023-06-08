from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializer
from .models import Books,Category
from django.http import Http404


class CategoriesView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer

    def get_object(self):
        try:
            return Books.objects.get(id=self.kwargs['name'])
        except Books.DoesNotExist:
            raise Http404("Book not found")


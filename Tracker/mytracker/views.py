from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializer
from .models import Books,Category
from django.http import Http404


class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategorySingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category'

    def get_object(self):
        try:
            category = self.kwargs['category']
            obj = self.get_queryset().get(category=category)
            self.check_object_permissions(self.request, obj)
            return obj
        except Category.DoesNotExist:
            raise Http404("Catgeory does not exist")

class BookView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'title'

    def get_object(self):
        try:
            title = self.kwargs['title']
            obj = self.get_queryset().get(title=title)
            self.check_object_permissions(self.request, obj)
            return obj
        except Books.DoesNotExist:
            raise Http404("Book not found")


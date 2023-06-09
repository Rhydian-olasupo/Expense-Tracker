from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializer
from .models import Books,Category
from django.http import Http404
from .forms import BookingForm
import requests


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


def books(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'books.html',context)


'''def book_list(request):
    response = requests.get('http://127.0.0.1:8000/api/booklist')

    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request,'booklist.html',{'Books':data})
    else:
        error_message = f'Error: {response.status_code}'
        return render(request,'error.html',{'message':error_message})'''
    
def book_list(request):
    url = 'http://127.0.0.1:8000/api/booklist'
    books = []  # List to store all books

    while url:
        # Make a GET request to the backend API
        response = requests.get(url)

        # Check the response status code
        if response.status_code == 200:
            # API request was successful
            data = response.json()  # Extract the JSON data from the response

            books.extend(data['results'])  # Add books to the list

            # Check if there is a next page
            url = data['next']
        else:
            # API request encountered an error
            error_message = f'Error: {response.status_code}'
            return render(request, 'error.html', {'message': error_message})

    # Pass the book data to the template for rendering
    return render(request, 'booklist.html', {'books': books})

from django.urls import path
from . import views 

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('category/<str:category>',views.CategorySingleView.as_view()),
    path('booklist',views.BookView.as_view()),
    path('books/<str:title>',views.SingleBookView.as_view()),
    #path('book/', views.books, name="book"),
    path('book/', views.BookView1.as_view()),
    path('books/',views.book_list,name='book-list')
]
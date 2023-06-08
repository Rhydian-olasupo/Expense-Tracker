from django.urls import path
from . import views 

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('books',views.BookView.as_view()),
    path('books/<str:name>',views.SingleBookView.as_view(),)
]
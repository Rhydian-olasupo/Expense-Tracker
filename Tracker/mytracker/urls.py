from django.urls import path
from . import views 

urlpatterns = [
    path('category', views.CategoriesView.as_view()),
    path('category/<str:category>',views.CategorySingleView.as_view()),
    path('books',views.BookView.as_view()),
    path('books/<str:title>',views.SingleBookView.as_view(),)
]
from .models import Category, Books
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category']

class BookSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.category')
    class Meta:
        model = Books
        fields = ['id','title','subtitle','authors','publisher','published_date','category','distribution_expense']


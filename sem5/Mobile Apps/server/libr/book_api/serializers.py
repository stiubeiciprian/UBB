from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'number_of_pages', 'current_page', 'genres')
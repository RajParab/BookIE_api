from django.shortcuts import render
from .models import Book, Chapter
from .serializers import BookSerializer, ChapterSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class ChapterViewSet(viewsets.ModelViewSet):
	#queryset=Chapter.objects.filter(bookName__slug__contains=slug)
	serializer_class=ChapterSerializer
	def get_queryset(self):
		slug = self.request.query_params.get('slug')
		queryset=Chapter.objects.filter(bookName__slug__contains=slug)
		return queryset

	
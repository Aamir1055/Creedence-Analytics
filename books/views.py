from django.shortcuts import render

# Create your views here.
# books/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is the root page.")


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

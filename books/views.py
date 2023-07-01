from django.shortcuts import render
from .models import Books ,Pages
# Create your views here.
from .serializers import bookSerlizer , pageSerlizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http.response import JsonResponse


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = bookSerlizer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = bookSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def pages(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pags = Pages.objects.all()
        serializer = pageSerlizer(pags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = pageSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

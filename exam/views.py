from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import IELTSExam,Book,Test
from .serializers import (ExamSerializer,BookSerializer
)
from django.contrib.auth import authenticate,login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
import re
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action

from ippanel import Client
from ippanel import HTTPError, Error, ResponseCode
from rest_framework import viewsets
from drf_spectacular.types import OpenApiTypes

    
class ExamViewSet(viewsets.ViewSet):
    queryset = IELTSExam.objects.all()
    serializer_class = ExamSerializer

    @extend_schema(description="Retrieve a list of services.",responses=ExamSerializer)
    def list(self, request):
        data = self.queryset
        serializer = self.serializer_class(data, many=True)
        response = Response(serializer.data, status=200)
        # Add debug print statements here
        print("Data:", data)
        print("Serialized Data:", serializer.data)
        return response
    
    def retrieve(self,request,pk):
        serializer= ExamSerializer(self.queryset.filter(id=pk),many=True)
        response=Response(serializer.data)
        return response
        
    
    @action(methods=['get'], detail=False, url_path=r"(?P<book_id>\w+)/all")
    def list_books_by_exam(self, request, book_id):
        serializer = ExamSerializer(self.queryset.filter(book=book_id), many=True)

        return Response(serializer.data)
    
    
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
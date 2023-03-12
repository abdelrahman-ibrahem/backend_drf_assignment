from django.shortcuts import render
from rest_framework import generics, permissions
from .seriailzers import  TaskSerializers
from .models import Task
from rest_framework.pagination import PageNumberPagination

# add pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ListCreateTask(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = TaskSerializers


class RetrevieUpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
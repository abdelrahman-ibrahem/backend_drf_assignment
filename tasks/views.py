from django.shortcuts import render
from rest_framework import generics, permissions
from .seriailzers import  TaskSerializers
from .models import Task



class ListCreateTask(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers


class RetrevieUpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
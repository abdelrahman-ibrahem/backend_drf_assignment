from django.shortcuts import render
from rest_framework import generics, permissions
from .seriailzers import  TaskSerializers
from .models import Task
from .filters import TaskFilter


class ListCreateTask(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filterset_class = TaskFilter


class RetrevieUpdateDeleteTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
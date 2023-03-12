from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreateTask.as_view()),
    path('<int:pk>/', views.RetrevieUpdateDeleteTask.as_view()),
]
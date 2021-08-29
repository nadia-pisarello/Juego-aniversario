from django.urls import path
from . import views

app_name = "preguntas"

urlpatterns = [
	path('crear/', views.crear, name = "crear"),
	path('', views.listar, name="listar"),
]
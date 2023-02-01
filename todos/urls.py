from django.urls import path
from .views import TodosView, delete_todo

app_name = 'todos'

urlpatterns = [
    path("", TodosView.as_view(), name='todos_view'),
    path("delete/<int:pk>", delete_todo, name='delete_todo'),
]

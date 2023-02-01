from django.urls import path
from .views import TodosView, DeleteTodo

app_name = 'todos'

urlpatterns = [
    path("", TodosView.as_view(), name='todos_view'),
    path("delete/<int:pk>", DeleteTodo.as_view(), name='delete_todo'),
]

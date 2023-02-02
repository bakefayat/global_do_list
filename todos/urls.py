from django.urls import path
from .views import TodosView, DeleteTodo, ChangeStatus

app_name = 'todos'

urlpatterns = [
    path("", TodosView.as_view(), name='todos_view'),
    path("delete/<str:uuid>", DeleteTodo.as_view(), name='delete_todo'),
    path("change/<str:uuid>", ChangeStatus.as_view(), name='change_todo'),
]

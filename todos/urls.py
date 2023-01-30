from django.urls import path
from .models import Todos
from .views import TodosView


urlpatterns = [
    path("", TodosView.as_view(), name='todos_view'),
]

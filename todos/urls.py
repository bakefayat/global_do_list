from django.urls import path
from .models import Todos
from .views import HomeView


urlpatterns = [
    path("", HomeView.as_view(), name='home'),
]

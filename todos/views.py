from django.shortcuts import render
from django.views.generic import View
from .models import Todos
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        todo_items = Todos.objects.all()
        return render(request, "todos/base.html", {'items': todo_items})

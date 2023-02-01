from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from core.utils import create_new_task
from .forms import TodosForm
from .models import Todos
# Create your views here.


class TodosView(View):
    def get(self, request, *args, **kwargs):
        todo_form = TodosForm()
        todo_items = Todos.objects.all()
        context = {'form': todo_form, 'items': todo_items}
        return render(request, "todos/base.html", context)

    def post(self, request, *args, **kwargs):
        title_of_task = request.POST.get('title')
        create_new_task(title_of_task)
        todo_form = TodosForm()
        todo_items = Todos.objects.all()
        context = {'form': todo_form, 'items': todo_items}
        return render(request, "todos/base.html", context)


def delete_todo(request, pk):
    todo = get_object_or_404(Todos, pk=pk)
    todo.delete()

    return redirect('todos:todos_view')

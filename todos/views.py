from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, RedirectView

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


class DeleteTodo(RedirectView):
    pattern_name = 'todos:todos_view'

    def get_redirect_url(self, *args, **kwargs):
        todo = get_object_or_404(Todos, unique_id=kwargs['uuid'])
        todo.delete()
        return super().get_redirect_url()


class ChangeStatus(RedirectView):
    pattern_name = 'todos:todos_view'

    def get_redirect_url(self, *args, **kwargs):
        todo = get_object_or_404(Todos, unique_id=kwargs['uuid'])
        if todo.status == 0:
            todo.status = 1
        else:
            todo.status = 0
        todo.save()
        return super().get_redirect_url()

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import RedirectView, CreateView

from .forms import TodosForm
from .models import Todos


class TodosView(CreateView):
    form_class = TodosForm
    success_url = reverse_lazy('todos:todos_view')
    template_name = 'todos/index.html'

    def get_context_data(self, **kwargs):
        kwargs['items'] = Todos.objects.all()
        return super(TodosView, self).get_context_data(**kwargs)


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

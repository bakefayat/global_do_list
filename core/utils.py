from todos.models import Todos


def create_new_task(title, *args, **kwargs):
    Todos.objects.create(title=title, *kwargs)

from todos.models import Todos
import uuid


def create_new_task(title, *args, **kwargs):
    Todos.objects.create(title=title, unique_id=uuid.uuid4())

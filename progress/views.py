from django.shortcuts import render
from .tasks import go_to_sleep

# Create your views here.
def index(request):
    task = go_to_sleep.delay(1)
    return render(request, 'progress/index.html', {'task_id': task.task_id})
from django.urls import path, include
from .views import categories, update_task_status

app_name = 'category'

urlpatterns = [
    path('', categories, name='my_categories'),
    path('update_task_status/<int:todo_id>/', update_task_status, name='update_task_status'),
]
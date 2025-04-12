from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import date
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .models import Category
from todolist.models import TodoList
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def categories(request):
    user = request.user
    now = timezone.now().date()
    todos = TodoList.objects.filter(user=user)
    categories = Category.objects.all()
    
    # Add status flags to each todo
    for todo in todos:
        # Handle both DateField and DateTimeField
        todo.due_date_date = todo.due_date.date() if hasattr(todo.due_date, 'date') else todo.due_date
        todo.is_overdue = todo.due_date_date and todo.due_date_date < now
        todo.is_pending = not todo.is_completed and not todo.is_overdue
    
    if request.method == "POST":
        # Add Task
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date_str = request.POST["date"]
            time = request.POST["time"]
            category = request.POST["category_select"]
            content = f"{title} at {time} on {date_str} [{category}]"
            
            TodoList.objects.create(
                title=title,
                content=content,
                time=time,
                due_date=date_str,
                category=Category.objects.get(name=category),
                user=user,
                is_completed=False
            )
            messages.success(request, "Task added successfully!")
            return redirect('category:my_categories')
            
        # Delete Task(s)
        if "taskDelete" in request.POST:
            checked_boxes = request.POST.getlist("checkedbox")
            
            if not checked_boxes:
                messages.warning(request, "Please select task(s) to delete")
            else:
                deleted_count, _ = TodoList.objects.filter(
                    id__in=checked_boxes,
                    user=user
                ).delete()
                
                if deleted_count:
                    messages.success(request, f"Deleted {deleted_count} task(s)")
                else:
                    messages.warning(request, "No tasks were deleted")
            return redirect('category:my_categories')
            
        # Update Task
        if "taskUpdate" in request.POST:
            task_id = request.POST.get("task_id")
            title = request.POST.get("description")
            date_str = request.POST.get("date")
            time = request.POST.get("time")
            category = request.POST.get("category_select")
            is_completed = request.POST.get("is_completed") == "on"  # Checkbox handling
            
            task = get_object_or_404(TodoList, id=task_id, user=user)
            
            task.title = title
            task.due_date = date_str
            task.time = time
            task.category = Category.objects.get(name=category)
            task.is_completed = is_completed  # Update completion status
            task.content = f"{title} at {time} on {date_str} [{category}]"
            task.save()
            
            messages.success(request, "Task updated successfully!")
            return redirect('category:my_categories')

    context = {
        "DateNow": now.strftime("%Y-%m-%d"),
        "todos": todos,
        "categories": categories,
    }
    return render(request, "category/category.html", context)

@require_POST
@login_required
def update_task_status(request, todo_id):
    try:
        data = json.loads(request.body)
        todo = get_object_or_404(TodoList, id=todo_id, user=request.user)
        todo.is_completed = data.get('is_completed', False)
        todo.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
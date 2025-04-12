from django import forms
from .models import TodoList
from category.models import Category

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TodoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = TodoList
        fields = ['title', 'content', 'category', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input rounded-md shadow-sm'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-input rounded-md shadow-sm'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md shadow-sm',
                'rows': 3
            }),
        }
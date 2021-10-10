from django import forms
from myproject.myapp.features.Todo.model.TodoModel import TodoTask as mModel


# Book Form
class TodoCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'

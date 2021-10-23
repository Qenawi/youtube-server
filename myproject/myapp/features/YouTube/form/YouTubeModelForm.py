from django import forms
from myproject.myapp.features.Todo.model.TodoModel import TodoTask as mModel


# Youtube Form
class YouTubeModelCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'

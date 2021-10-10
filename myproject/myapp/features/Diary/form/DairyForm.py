from django import forms
from myproject.myapp.features.Diary.model.DiaryModel import DiaryModel as mModel


# Book Form
class DiaryCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'

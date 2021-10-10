from django import forms
from myproject.myapp.features.LifeEvents.model.LifeEventModel import LifeEvent as mModule


# Book Form
class LifeEventCreate(forms.ModelForm):
    class Meta:
        model = mModule
        fields = '__all__'

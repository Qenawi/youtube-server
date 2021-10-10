from django import forms
from myproject.myapp.features.Analytics.model.AnalyticModule import AnalyticModule as mModule


# Book Form
class AnalyticCreate(forms.ModelForm):
    class Meta:
        model = mModule
        fields = '__all__'

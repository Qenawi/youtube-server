from django import forms
from myproject.myapp.features.YouTube.model.YouTubeModel import YoutubeModel as mModel


# Youtube Form
class YouTubeModelCreate(forms.ModelForm):
    class Meta:
        model = mModel
        fields = '__all__'

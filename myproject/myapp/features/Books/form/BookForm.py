from django import forms
from myproject.myapp.features.Books.model.BookModel import BookModel as mModule


# Book Form
class BookCreate(forms.ModelForm):
    class Meta:
        model = mModule
        fields = '__all__'

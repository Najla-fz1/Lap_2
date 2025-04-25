from django import forms
from . import models 

class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'book title',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )     
    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0
    )
    edition = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput()
    )
    class Meta:
        model = models.Book  # ربط الفورم بالمودل
        fields = ['title', 'author', 'price', 'edition']

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields= ['title','author','description','genre','isbn','publications_date']

        widgets={
            'title':forms.TextInput(attrs={'clss':'form-control','placeholder':'Enter book title'}),
            'author':forms.TextInput(attrs={'clss':'form-control','placeholder':'Enter author name'}),
            'description':forms.TextInput(attrs={'clss':'form-control','rows':4,'placeholder':'Enter book desscription'}),

            'isbn':forms.TextInput(attrs={'clss':'form-control','placeholder':'Enter ISBN'}),
            'publications_date':forms.TextInput(attrs={'clss':'form-control','type':'date'}),
            
        }
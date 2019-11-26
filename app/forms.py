from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','age','sex','course','year','memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：山田　太郎'}),
                    'age': forms.NumberInput(attrs={'min':1}),
                    'sex': forms.RadioSelect(),
                    'course': forms.RadioSelect(),
                    'year': forms.RadioSelect(),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }

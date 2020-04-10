from django import forms

from .models import Congress, TypeCongress

class CongressCreateForm(forms.ModelForm):

    class Meta:
        model = Congress
        fields = ['username', 'name', 'type_congress']

class TypeCongressCreateForm(forms.ModelForm):

    class Meta:
        model = TypeCongress
        fields = ['type_congress', ]

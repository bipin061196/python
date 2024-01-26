from django import forms
from .models import Server, Specification

class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['text']
        labels = {'text':''}

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = Specification
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
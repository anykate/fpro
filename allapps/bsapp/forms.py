from django import forms
from .models import Language, Framework


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class FrameworkForm(forms.ModelForm):
    class Meta:
        model = Framework
        fields = '__all__'

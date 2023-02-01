from django import forms
from .models import NewsTitle
from django.forms import ModelForm

class SaveTitleForm(ModelForm):
    class Meta:
        model = NewsTitle
        fields = "__all__"
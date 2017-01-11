from django import forms
from . import models
from .models import *


class PackageForm(forms.ModelForm):
    # color = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Color.objects.all()
    #     )

    class Meta:
        model = Package

        fields = [
            'color',
            'coffee',
            'description',
            'image'
        ]

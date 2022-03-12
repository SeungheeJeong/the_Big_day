from django import forms
from .models import Maps


class MapsForm(forms.ModelForm):
    class Meta:
        model = Maps
        fields = ['category', 'name', 'kakaourl', 'pageurl']

from .models import *
from django import forms

class YorumForm(forms.ModelForm):
    
    class Meta:
        model = Yorum
        fields = ["icerik"]

        widgets = {
            'icerik': forms.Textarea(attrs={'class':'form-control'}),
        }

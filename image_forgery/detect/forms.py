from django import forms
from .models import detectedimages
from django.contrib.auth.models import User



class imageForm(forms.ModelForm):
    class Meta:
        model = detectedimages
        fields = ('id','sample_image')
from django import forms

from .models import MyVideo


class MyVideoForm(forms.ModelForm):
    url = forms.CharField(max_length=300, help_text="Enter your Youtube Url here")

    class Meta:
        model = MyVideo
        fields = ('url',)

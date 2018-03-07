from django import forms
from . import models

class CreatePost(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ceritakan isi hatimu. Max 100 karakter', 'autofocus':True, 'maxlength':100, 'rows':5}))

    class Meta:
        model = models.Post
        fields = ['body']
from django import forms

from pets.models import Pet, Comments


class CreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea())


from django import forms
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = ContactMe
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
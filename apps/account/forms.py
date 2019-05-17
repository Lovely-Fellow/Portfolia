from django import forms

from .models import Subscriber


class SubscriberAddForm(forms.ModelForm):
    name = forms. CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        max_length=50,
    )

    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
        max_length=100,
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 100, 'cols': 25, 'placeholder': 'Message'}),
        max_length=1500
    )

    class Meta:
        model = Subscriber
        fields = ('name', 'email', 'subject', 'message')


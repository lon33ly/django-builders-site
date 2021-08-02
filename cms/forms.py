from .models import Requests
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class RequestsForm(ModelForm):
    class Meta:
        model = Requests
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'id': 'name',
                'placeholder': 'Имя'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
                'placeholder': 'Email'
            }),
            "subject": TextInput(attrs={
                'class': 'form-control',
                'name': 'subject',
                'id': 'subject',
                'placeholder': 'Тема'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'name': 'message',
                'id': 'message',
                'placeholder': 'Сообщение',
                'cols': '30',
                'rows': '4'
            })
        }
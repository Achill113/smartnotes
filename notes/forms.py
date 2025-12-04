from django import forms

from .models import Note

class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        labels = {
            'text': 'Write your thoughts here'
        }
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
                'text': forms.Textarea(attrs={'class': 'form-control my-5'})
        }

from django.forms import ModelForm, Textarea
from .models import CodeSnippet


class NameForm(ModelForm):
    class Meta:
        model = CodeSnippet
        fields = ['text']
        widgets = {
            "text": Textarea(attrs={'cols': 120, 'rows': 30}),
        }

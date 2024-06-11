from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .models import CodeSnippet
from .forms import NameForm


class SnippetCreateView(CreateView):
    model = CodeSnippet
    form_class = NameForm
    template_name = 'create.html'



class SnippetDetailView(DetailView):
    model = CodeSnippet
    template_name = 'detail.html'






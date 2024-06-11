from django.urls import path
from .views import SnippetCreateView, SnippetDetailView


urlpatterns = [
    path('', SnippetCreateView.as_view(), name='create'),
    path('<slug:slug>/', SnippetDetailView.as_view(), name='detail'),
]

from django import forms
from .models import Question, Comment
import json
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

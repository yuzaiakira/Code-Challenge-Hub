from django import forms
from challenge.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['user', 'name', 'file']

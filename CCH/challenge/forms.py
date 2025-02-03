from django import forms
from challenge.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input_class bg-[#333C4C] font-medium',
                'id': 'question',
                'placeholder': 'شماره سوال یا نام فایل را وارد نمایید ...'
            }),
            'file': forms.FileInput(attrs={
                'class': 'input_class h-full opacity-0 font-medium',
                'id': 'file'
            })
        }
        labels = {
            'name': '',  # Remove label for name field
            'file': ''   # Remove label for file field
        }

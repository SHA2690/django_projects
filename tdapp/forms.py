from django import forms
from tdapp.models import Todo
class TodoForm(forms.ModelForm):
    task = forms.CharField(max_length=100)
    class Meta:
        model = Todo
        fields = '__all__'

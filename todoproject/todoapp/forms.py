
from . models import Task
from django import  forms

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','dob','gender','age','txt','phone','materials']


from django import forms 
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['roll','name']
        # exclude = ['roll']
        labels = {
            'roll': 'Student Roll', 
            'name': 'Student Name'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
        }
        help_texts = {
            'name' : 'Write your full Name.'
        }
        error_messages = {
            'name' : {'required' : 'Your name is required!'}
        }
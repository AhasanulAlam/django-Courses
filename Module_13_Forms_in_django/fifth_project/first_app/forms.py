from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="User Name", initial='', help_text='Total length must be 70 characters', required=False, disabled=False, widget=forms.Textarea(attrs= {'id' : 'test_area', 'class' : 'myClass1 myClass2', 'placeholder' : 'Enter your Name.'}))
    # file = forms.FileField()
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    # birthday = forms.DateField(label="Date Of Birth")
    birthday = forms.CharField(label="Date Of Birth", widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs = {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]
    # size = forms.ChoiceField(choices = CHOICES)
    size = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'),('M', 'Mushroom'),('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices = MEAL)
    pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)


# class StudentData(forms.Form):
#     name = forms.CharField(label="User Name", widget=forms.TextInput)
#     email = forms.CharField(label="User Email", widget=forms.EmailInput)
#     # def clean_name(self):
#     #     nameValue = self.cleaned_data['name']
#     #     if len(nameValue) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")
#     #     return nameValue
#     # def clean_email(self):
#     #     emailValue = self.cleaned_data['email']
#     #     if '.com' not in emailValue:
#     #         raise forms.ValidationError("Enter a valid email with .com")
#     #     return emailValue
#     def clean(self):
#         cleaned_data = super().clean()
#         nameValue = self.cleaned_data['name']
#         emailValue = self.cleaned_data['email']
#         if len(nameValue) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         if '.com' not in emailValue:
#             raise forms.ValidationError("Enter a valid email with .com")
        

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 Characters!")


class StudentData(forms.Form):
    # name = forms.CharField(label="User Name", widget=forms.TextInput, validators=[validators.MaxLengthValidator(10 , message="Enter a name with at Max 10 characters")])
    name = forms.CharField(label="User Name", widget=forms.TextInput, validators=[validators.MinLengthValidator(10 , message="Enter a name with at least 10 characters")])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(label="User Email", widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(34, message="Age must be max 34"), validators.MinValueValidator(18, message="Age must be at least 18")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File extension must be with .pdf or .png')])




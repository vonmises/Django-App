from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        exclude = ['last_update']
        model = Student

    def clean_age(self):
        age = self.cleaned_data.get('age')

        if age > 120:
            raise forms.ValidationError('You may be too old for this class')
        elif age < 10:
            raise forms.ValidationError('You may be too young for this class')

        return age

class FeedbackForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput({
                 "class": "form-control",
                 "placeholder": "First Name",
                 }))
    last_name = forms.CharField(widget=forms.TextInput({
                "class": "form-control",
                "placeholder": "Last Name",
                }))
    email = forms.EmailField(widget=forms.TextInput({
                "class": "form-control",
                "placeholder": "Email",
                }))
    message = forms.CharField(widget=forms.Textarea({
              "class": "form-control",
              "placeholder": "Feedback",
              }))

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message.lower() == 'dirty':
            message = "Clean"

        return message

from django import forms
from django.core.exceptions import ValidationError


class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)
    confirm_password = forms.CharField(max_length=100, required=True)
    student_id = forms.IntegerField(required=True)
    university = forms.CharField(max_length=100, required=True)

    def clean(self):
        if self.data['password'] != self.data['confirm_password']:
            raise ValidationError('Entered passwords do not match')

        return self.cleaned_data
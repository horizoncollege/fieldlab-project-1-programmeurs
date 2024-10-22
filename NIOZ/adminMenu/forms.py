from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = Person
        fields = ['username', 'realName', 'password1', 'password2']  # Updated 'email' to 'realName'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        person = super().save(commit=False)
        person.password = self.cleaned_data['password1']  # You can hash the password here if needed
        if commit:
            person.save()
        return person
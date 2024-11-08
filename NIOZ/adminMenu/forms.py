from django import forms
from .models import Person
from django.contrib.auth.hashers import make_password  # Zorg ervoor dat je dit import

class PersonForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = Person
        fields = ['realName', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        person = super().save(commit=False)
        # Hier hash je het wachtwoord
        person.password = make_password(self.cleaned_data['password1'])  # Hash het wachtwoord
        if commit:
            person.save()
        return person

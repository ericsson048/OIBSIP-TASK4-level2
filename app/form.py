from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import ProfileUser


class SignupForm(UserCreationForm):

    class Meta:
        model = ProfileUser
        fields = UserCreationForm.Meta.fields + \
            ('username', 'first_name', 'last_name', 'date_of_birth','email')

    def try_save(self, request):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if ProfileUser.objects.filter(email=email).exists():
            raise forms.ValidationError("this mail is alread used.")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, required=True)
    email = forms.EmailField(label='email', max_length=254, required=True)
    password = forms.CharField(label="Password1", max_length=30, required=True, widget=forms.PasswordInput)



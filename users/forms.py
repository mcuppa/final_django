# en forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CustomPasswordChangeForm(UserChangeForm):
    new_password1 = forms.CharField(label="New password", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'new_password1']

    def clean_new_password1(self):
        return self.cleaned_data.get('new_password1')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['email'].help_text = None
        self.fields['first_name'].help_text = None
        self.fields['last_name'].help_text = None
        self.fields['new_password1'].help_text = None
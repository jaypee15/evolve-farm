from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "phone_number"
            
            )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            
            )


class CustomSignupForm(SignupForm):

    phone_number = forms.CharField(max_length=100, required=True)

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data["phone_number"]

        user.save()
        return user
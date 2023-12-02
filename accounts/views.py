from allauth.account.views import SignupView
from .forms import CustomSignupForm

class CustomSignupView():
    form_class = CustomSignupForm
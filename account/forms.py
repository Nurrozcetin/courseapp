from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.forms import ValidationError, widgets
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if username == "fatmanurozcetin":
            messages.add_message(self.request, messages.SUCCESS, "Welcome feytos")
        return username
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("a"):
            raise ValidationError("You cannot enter a username starting with this letter")
        
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ("username", "email",)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email = email).exists():
            self.add_error("email", "This email used before")
        return email
    
    def clean_password2(self):
        super().clean_password2()
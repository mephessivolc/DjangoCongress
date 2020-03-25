from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _
from django import forms


Users = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _(
            "Por favor entre com um usuario ou email e senha corretos. Note que ambos "
            "os campos diferenciam entre letras maiúsculas e minúsculas."
        ),
        'inactive': _("This account is inactive."),
    }

class UserAdminCreateForm(UserCreationForm):

    class Meta:
        model = Users
        fields = ['name', 'email', 'cpf', 'ie', 'course', 'nivel', 'tshirt']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['name', 'email', 'cpf', 'ie', 'course', 'nivel']

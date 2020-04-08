from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, views, update_session_auth_hash, mixins
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

from .forms import UserAdminCreateForm, UserUpdateForm

Users = get_user_model()

class IndexView(TemplateView):
    template_name = 'users/index.html'

class CreateUsersView(CreateView):
    model = Users
    form_class = UserAdminCreateForm
    success_url = reverse_lazy('core:index')
    template_name = 'users/create.html'

class LoginUsersView(LoginView):
    template_name = 'users/login.html'
    # success_url = reverse_lazy('core:index')

class LogoutUsersView(mixins.LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('core:index')

class UpdateUsersView(mixins.LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:index')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Atualizado com sucesso')

        return super(UpdateUsersView, self).get_success_url()

class UpdatePasswordView(mixins.LoginRequiredMixin, FormView):
    template_name = 'users/update_password.html'

    def post(self, request, *args, **kwargs):
        form = views.PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            messages.success(request, 'Senha alterada com sucesso')

            return redirect('users:index')

        else:
            messages.error(request, 'Por favor verifique os erros abaixo.')

    def get(self, request, *args, **kwargs):
        form = views.PasswordChangeForm(request.user)

        return render(request, self.template_name, {
            'form': form,
        })

class PasswordResetView(views.PasswordResetView):

    template_name = 'users/password_reset_form.html'
    subject_template_name = 'users/password_reset_subject.txt'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class PasswordResetDoneView(views.PasswordResetDoneView):

    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(views.PasswordResetConfirmView):

    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class PasswordResetCompleteView(views.PasswordResetCompleteView):

    template_name = 'users/password_reset_complete.html'

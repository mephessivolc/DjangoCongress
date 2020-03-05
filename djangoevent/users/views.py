from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import ( LoginView, LogoutView, PasswordChangeForm,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import (TemplateView, CreateView, FormView,
    UpdateView)

from .forms import UserAdminCreateForm, CustomAuthenticationForm, UserUpdateForm
from .models import Users
from .resources import UsersNameResources, UsersNameEmailResources
from .report_pdf import ReportListUsersPDF, ReportListUsersEmailPDF


class CreateUsers(CreateView):
    template_name = 'users/register.html'
    form_class = UserAdminCreateForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)

        context['title'] = 'Cadastrar'

        return context

    def get_success_url(self):
        msg = 'Cadastro feito com sucesso'
        messages.success(self.request, mark_safe(msg))

        return super(CreateView, self).get_success_url()

class LoginUsers(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super(LoginUsers, self).get_context_data(**kwargs)

        context['title'] = 'Entrar'

        return context

class LogoutUsers(LogoutView):
    next_page = reverse_lazy('core:index')

class UpdatePasswordUserView(LoginRequiredMixin, FormView):
    template_name = 'users/register_password.html'

    def get_context_data(self, **kwargs):
        context = super(UpdatePasswordUserView, self).get_context_data(**kwargs)

        context['title'] = 'Alterar senha'

        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            messages.success(request, 'Senha alterada com sucesso')

            return redirect('core:index')

        else:
            messages.error(request, 'Por favor verifique os erros abaixo.')

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)

        return render(request, self.template_name, {
            'title': 'Alterar Senha',
            'form': form,
        })

class PasswordUserResetView(PasswordResetView):

    template_name = 'users/password_reset_form.html'
    subject_template_name = 'users/password_reset_subject.txt'
    email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')


class PasswordUserResetDoneView(PasswordResetDoneView):

    template_name = 'users/password_reset_done.html'


class PasswordUserResetConfirmView(PasswordResetConfirmView):

    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class PasswordUserResetCompleteView(PasswordResetCompleteView):

    template_name = 'users/password_reset_complete.html'

class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'users/register.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:update_user')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, 'Cadastro atualizado com sucesso')

        return super(UpdateUserView, self).get_success_url()

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)

        context['title'] = 'Atualizar'

        return context

class UserCSVNameList(TemplateView):

    def render_to_response(self, context, **response_class):
        list_users = UsersNameResources()
        database = list_users.export()

        response = HttpResponse(database.csv, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename="usersName.csv"'
        return response

class UserCSVNameEmailList(TemplateView):

    def render_to_response(self, context, **response_class):
        list_users = UsersNameEmailResources()
        database = list_users.export()

        response = HttpResponse(database.csv, content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename="usersNameEmail.csv"'

        return response

class UserPDFNameList(TemplateView):

    def render_to_response(self, context, **response_class):
        pdf = ReportListUsersPDF(pdf_name='ListaPresenca')
        pdf.set_title_page('Lista de Inscrição Completa')
        pdf.set_query(Users.objects.all())

        return pdf.get_document()

class UserPDFNameEmailList(TemplateView):

    def render_to_response(self, context, **response_class):
        pdf = ReportListUsersEmailPDF(
            title_page='Lista de E-mail Completo',
            query=Users.objects.all()
        )
        pdf.set_pdf_name('ListaEmail')
        # pdf.set_title_page('Lista de E-mail')

        return pdf.get_document()

class UserPDFNameSubscribedList(TemplateView):

    def render_to_response(self, context, **response_class):
        pdf = ReportListUsersPDF(
            title_page='Lista de Inscritos',
            sub_title = 'RECEBEM kit de inscrição',
            query=Users.objects.filter(is_payment=True)
        )
        pdf.set_pdf_name('ListaInscritosComKit')
        # pdf.set_title_page('Lista de E-mail')

        return pdf.get_document()

class UserPDFNameNoSubscribedList(TemplateView):

    def render_to_response(self, context, **response_class):
        pdf = ReportListUsersPDF(
            title_page='Lista de Inscritos',
            sub_title = 'SEM kit de inscrição',
            query=Users.objects.filter(is_payment=False)
        )
        pdf.set_pdf_name('ListaInscritosSemKit')

        return pdf.get_document()

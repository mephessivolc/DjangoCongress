from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import mixins

from .forms import CongressCreateForm, TypeCongressCreateForm
from .models import Congress, TypeCongress
# Create your views here.

class Index(TemplateView):
    template_name = 'core/index.html'

class CongressCreateView(CreateView):
    template_name = 'core/create.html'
    form_class = CongressCreateForm
    model = Congress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento cadastrado com sucesso')

        return super(CongressCreateView, self).get_success_url()

class TypeCongressCreateView(CreateView):
    template_name = 'core/create.html'
    form_class = TypeCongressCreateForm
    model = TypeCongress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Tipo cadastrado com sucesso')

        return super(TypeCongressCreateView, self).get_success_url()

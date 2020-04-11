from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import ( TemplateView, CreateView, UpdateView,
        FormView, ListView, DetailView
    )
from django.contrib.auth.views import LoginView
from django.contrib.auth import mixins

from .forms import CongressCreateUpdateForm, TypeCongressCreateUpdateForm
from .models import Congress, TypeCongress
# Create your views here.

class Index(TemplateView):
    template_name = 'core/index.html'

class CongressIndex(LoginView, TemplateView):
    template_name = 'core/congress.html'

class CongressCreateView(LoginView, CreateView):
    template_name = 'core/create.html'
    form_class = CongressCreateUpdateForm
    model = Congress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento cadastrado com sucesso')

        return super(CongressCreateView, self).get_success_url()

class CongressUpdateView(LoginView, UpdateView):
    template_name = 'core/update.html'
    form_class = CongressCreateUpdateForm
    model = Congress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento atualizado com sucesso')

        return super(CongressUpdateView, self).get_success_url()

class CongressListView(LoginView, ListView):
    template_name = 'core/list.html'
    queryset = Congress.objects.all()

class CongressDetailView(LoginView, DetailView):
    template_name = 'core/detail.html'
    

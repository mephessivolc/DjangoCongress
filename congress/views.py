from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import mixins, get_user_model

from . import models, forms
from core import pdf
# Create your views here.

Users = get_user_model()
class Index(generic.TemplateView):
    template_name = 'congress/index.html'

class CongressIndex(LoginView, generic.TemplateView):
    template_name = 'congres/congress.html'

class CongressCreateView(LoginView, generic.CreateView):
    template_name = 'congress/create.html'
    form_class = forms.CongressCreateUpdateForm
    model = models.Congress
    success_url = reverse_lazy('congress:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento cadastrado com sucesso')

        return super(CongressCreateView, self).get_success_url()

class CongressUpdateView(LoginView, generic.UpdateView):
    template_name = 'congress/update.html'
    form_class = forms.CongressCreateUpdateForm
    model = models.Congress
    success_url = reverse_lazy('congress:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento atualizado com sucesso')

        return super(CongressUpdateView, self).get_success_url()

class CongressListView(LoginView, generic.ListView):
    template_name = 'congress/list.html'
    queryset = models.Congress.objects.all()

class CongressDetailView(LoginView, generic.DetailView):
    template_name = 'congress/detail.html'

class ReportPdf(pdf.TablePdfManager):
    filename = 'lista_presenca'
    title = 'Lista de Presença'
    data_list = Users.objects.all().order_by('name')
    congress_queryset = models.Congress.objects.first()

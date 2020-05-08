from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import mixins, get_user_model

from .forms import CongressCreateUpdateForm, TypeCongressCreateUpdateForm
from . import models, pdf
# Create your views here.

class Index(generic.TemplateView):
    template_name = 'core/index.html'

class CongressIndex(LoginView, generic.TemplateView):
    template_name = 'core/congress.html'

class CongressCreateView(LoginView, generic.CreateView):
    template_name = 'core/create.html'
    form_class = CongressCreateUpdateForm
    model = models.Congress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento cadastrado com sucesso')

        return super(CongressCreateView, self).get_success_url()

class CongressUpdateView(LoginView, generic.UpdateView):
    template_name = 'core/update.html'
    form_class = CongressCreateUpdateForm
    model = models.Congress
    success_url = reverse_lazy('core:index')

    def get_success_url(self):
        messages.success(self.request, 'Evento atualizado com sucesso')

        return super(CongressUpdateView, self).get_success_url()

class CongressListView(LoginView, generic.ListView):
    template_name = 'core/list.html'
    queryset = models.Congress.objects.all()

class CongressDetailView(LoginView, generic.DetailView):
    template_name = 'core/detail.html'

class ImagesListView(LoginView, generic.ListView):
    model = models.Images
    template_name = 'core/images_list.html'

class ImagesDetailView(LoginView, generic.DetailView):
    model = models.Images
    template_name = 'core/images_detail.html'

Users = get_user_model()
class ReportPdf(pdf.TablePdfManager):
    filename = 'Lista de Presença'
    data_list = Users.objects.all()
    data_congress = models.Congress.objects.first()

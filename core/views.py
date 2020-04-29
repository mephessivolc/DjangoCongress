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

class ImagesCongressListView(LoginView, generic.ListView):
    model = models.ImagesCongress
    template_name = 'core/images_list.html'

class ImagesCongressDetailView(LoginView, generic.DetailView):
    model = models.ImagesCongress
    template_name = 'core/images_detail.html'

Users = get_user_model()
class ReportPdf(generic.TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Users.objects.all()
        context['extra_lines'] = 10
        # context['filename'] = 'Lista_presenca'
        # context['data'] = data

        return context

    def render_to_response(self, context, **response_kwargs):
        file_pdf = pdf.ListRender(**self.get_context_data())
        # return pdf.report(context, data)
        return file_pdf.render_to_response()

from django.contrib import messages
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'core/index.html'

class ListView(TemplateView):
    template_name = 'core/list.html'

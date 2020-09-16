from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'core/index.html'
index = IndexView.as_view()

class AdministracaoView(LoginRequiredMixin, TemplateView):
    template_name = 'core/administracao.html'
administracao = AdministracaoView.as_view()

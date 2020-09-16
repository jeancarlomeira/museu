from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages

from .models import  (
    Material,
    Colaborador,
    TipodeEntrada,
    TipodeArtefato,
    Ambiente,
    Artista
)

class MateriaisView(ListView):
    model = Material
    template_name = 'catalogo/materiais.html'
    context_object_name = 'materiais'
    paginate_by = 10
materiais = MateriaisView.as_view()


class MaterialView(DetailView):
    model = Material
    template_name = 'catalogo/material.html'
    context_object_name = 'material'

    def get_queryset(self):
        return Material.objects.filter(slug = self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        m = Material.objects.filter(slug = self.kwargs['slug'])
        c = self.get_object().colaborador
        a = self.get_object().artista
        colab = Colaborador.objects.get(nome=c)
        art = Artista.objects.get(nome=a)
        context = super().get_context_data(**kwargs)
        context['colab'] = colab
        context['art'] = art
        return context

material = MaterialView.as_view()

class ColaboradoresView(ListView):
    model = Colaborador
    template_name = 'catalogo/colaboradores.html'
    context_object_name = 'colaboradores'
    ordering = ['id']
colaboradores = ColaboradoresView.as_view()


class ColaboradorView(DetailView):
    model = Material
    template_name = 'catalogo/colaborador.html'
    context_object_name = 'colaborador'

    def get_queryset(self):
        return Colaborador.objects.filter(slug = self.kwargs['slug'])

colaborador = ColaboradorView.as_view()


class TipodeentradaView(ListView):
    model = TipodeEntrada
    template_name = 'catalogo/tipodeentrada.html'
    context_object_name = 'tipodeentrada'
    ordering = ['id']
tipodeentrada = TipodeentradaView.as_view()


class TipodeartefatoView(ListView):
    model = TipodeArtefato
    template_name = 'catalogo/tipodeartefato.html'
    context_object_name = 'tipodeartefato'
    ordering = ['id']
tipodeartefato = TipodeartefatoView.as_view()


class AmbientesView(ListView):
    model = Ambiente
    template_name = 'catalogo/ambientes.html'
    context_object_name = 'ambientes'
    ordering = ['id']
ambientes = AmbientesView.as_view()


class ArtistasView(ListView):
    model = Artista
    template_name = 'catalogo/artistas.html'
    context_object_name = 'artistas'
    ordering = ['id']
artistas = ArtistasView.as_view()

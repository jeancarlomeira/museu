from django.db import models
from django.urls import reverse
from django.forms.models import ModelForm


class Material(models.Model):
    codigo_registro = models.CharField('Código Registro', max_length=7, blank=False, unique=True)
    tipo_de_entrada = models.ForeignKey('catalogo.TipodeEntrada', verbose_name='Entradas', on_delete=models.PROTECT)
    tipo_de_artefato = models.ForeignKey('catalogo.TipodeArtefato', verbose_name='Artefatos', on_delete=models.PROTECT)
    ambiente = models.ForeignKey('catalogo.Ambiente', verbose_name='Ambientes', on_delete=models.PROTECT)
    colaborador = models.ForeignKey('catalogo.Colaborador', verbose_name='Colaboradores', related_name='colab',on_delete=models.PROTECT)
    titulo = models.CharField('Título', max_length=100)
    artista = models.ForeignKey('catalogo.Artista', verbose_name='Artistas', on_delete=models.PROTECT)
    descricao = models.TextField('Decrição', max_length=200)
    procedencia = models.TextField('Procedência:', max_length=200, default='')
    altura = models.DecimalField('Altura', max_digits=5, decimal_places=2, default='0')
    largura = models.DecimalField('Largura', max_digits=5, decimal_places=2, default='0')
    outras = models.CharField('Outras', max_length=100, blank=True)
    data_da_conclusao = models.DateField('Data da conclusão da peça', blank=True, null=True, default='')
    local = models.CharField('Local', max_length=100, blank=True)
    tecnica = models.CharField('Técnica', max_length=100, blank=True)
    suporte = models.CharField('Suporte', max_length=100, blank=True)
    moldura = models.CharField('Moldura', max_length=100, blank=True)
    valor_estimado_original = models.DecimalField('Valor Estimado Original (R$)', max_digits=8, decimal_places=2, default='0')
    ultimo_valor_estimado = models.DecimalField('Último Valor Estimado (R$)', max_digits=8, decimal_places=2, default='0')
    data_ultimo_valor_estimado = models.DateField('Data do último valor estimado', blank=True, null=True)
    posicao_assinatura = models.CharField('posição da assinatura', max_length=100,blank=True, null=True)
    historico_do_artefato = models.CharField('Histórico do artefato', max_length=100, blank=True)
    coletor = models.CharField('Coletor', max_length=100)
    data_da_catalogacao = models.DateField('Data da catalogação')
    catalogador = models.CharField('Catalogador', max_length=100)
    image = models.URLField('Imagem', max_length=800)
    slug = models.SlugField('Identificador', max_length=100, blank=False, unique=True, help_text="Preenchido automaticamente, não editar.")

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering = ['codigo_registro']

    def __str__(self):
        return self.codigo_registro

    def get_absolute_url(self):
        return reverse('catalogo:materiais', kwargs={'slug' : self.slug})

class Colaborador(models.Model):
    nome = models.CharField('Nome', max_length=100)
    profissao = models.CharField('Profissão', max_length=100, blank=True)
    idade = models.CharField('Idade', max_length=3, blank=True)
    endereco = models.CharField('Endereço', max_length=100, blank=True)
    contato = models.CharField('Contato', max_length=100, blank=True)
    data_do_termo = models.DateField('Data do termo', max_length=100, blank=True)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:colaborador', kwargs={'slug' : self.slug})

class TipodeEntrada(models.Model):
    nome = models.CharField('Tipo de Entrada', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:tipodeentrada', kwargs={'slug' : self.slug})

class TipodeArtefato(models.Model):
    nome = models.CharField('Tipo de artefato', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Artefato'
        verbose_name_plural = 'Artefatos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:tipodeartefato', kwargs={'slug' : self.slug})

class Ambiente(models.Model):
    nome = models.CharField('Ambiente', max_length=100)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:ambiente', kwargs={'slug' : self.slug})

class Artista(models.Model):
    nome = models.CharField('Artista', max_length=100)
    biografia = models.TextField('Biografia', max_length=500, blank=True)
    slug = models.SlugField('Identificador', max_length=100, unique=True, help_text="Preenchido automaticamente, não editar.",)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalogo:artista', kwargs={'slug' : self.slug})

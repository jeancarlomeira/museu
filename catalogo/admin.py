from django.contrib import admin

from .models import (
    Material,
    Colaborador,
    TipodeEntrada,
    TipodeArtefato,
    Ambiente,
    Artista
)

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['codigo_registro', 'tipo_de_entrada', 'tipo_de_artefato', 'ambiente', 'colaborador',
                    'titulo', 'artista', 'descricao', 'altura', 'largura', 'outras', 'data_da_conclusao',
                    'local', 'tecnica', 'suporte', 'moldura', 'valor_estimado_original', 'ultimo_valor_estimado',
                    'data_ultimo_valor_estimado', 'posicao_assinatura', 'historico_do_artefato',
                    'coletor', 'data_da_catalogacao', 'catalogador', 'image']
    search_fields = ['codigo_registro', 'titulo', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('codigo_registro',)}

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'profissao', 'idade', 'endereco', 'contato', 'data_do_termo']
    search_fields = ['nome', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('nome',)}

class TipodeEntradaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'created', 'modified']
    search_fields = ['nome', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('nome',)}

class TipodeArtefatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'created', 'modified']
    search_fields = ['nome', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('nome',)}

class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'created', 'modified']
    search_fields = ['nome', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('nome',)}

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'biografia', 'created', 'modified']
    search_fields = ['nome', 'slug']
    list_filter = ['created', 'modified']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Material, MaterialAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(TipodeEntrada, TipodeEntradaAdmin)
admin.site.register(TipodeArtefato, TipodeArtefatoAdmin)
admin.site.register(Ambiente, AmbienteAdmin)
admin.site.register(Artista, ArtistaAdmin)

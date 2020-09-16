from django.shortcuts import render
from django.db.models import Q
from catalogo.models import Material, Colaborador


def pesquisa(request):
    if request.method == 'GET':
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= (Q(titulo__icontains=query) | Q(codigo_registro__icontains=query) | Q(colaborador__nome__icontains=query) | Q(artista__nome__icontains=query)
                    | Q(ambiente__nome__icontains=query) | Q(tipo_de_entrada__nome__icontains=query) | Q(tipo_de_artefato__nome__icontains=query))

            object_list= Material.objects.filter(lookups).distinct()
            context={'object_list': object_list,'submitbutton': submitbutton}
            return render(request, 'pesquisa/pesquisa.html', context)
        else:
            return render(request, 'pesquisa/pesquisa.html')
    else:
        return render(request, 'pesquisa/pesquisa.html')

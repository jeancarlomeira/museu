# Generated by Django 2.2.2 on 2020-08-24 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='biografia',
            field=models.TextField(blank=True, max_length=500, verbose_name='Biografia'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='contato',
            field=models.CharField(blank=True, max_length=100, verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='data_do_termo',
            field=models.DateField(blank=True, max_length=100, verbose_name='Data do termo'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='idade',
            field=models.CharField(blank=True, max_length=3, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='profissao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Profissão'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='altura',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=5, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='data_da_conclusao',
            field=models.DateField(blank=True, default='', null=True, verbose_name='Data da conclusão da peça'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='data_ultimo_valor_estimado',
            field=models.DateField(blank=True, verbose_name='Data do último valor estimado'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='historico_do_artefato',
            field=models.CharField(blank=True, max_length=100, verbose_name='Histórico do artefato'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='largura',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=5, verbose_name='Largura'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='local',
            field=models.CharField(blank=True, max_length=100, verbose_name='Local'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='moldura',
            field=models.CharField(blank=True, max_length=100, verbose_name='Moldura'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='outras',
            field=models.CharField(blank=True, max_length=100, verbose_name='Outras'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='posicao_assinatura',
            field=models.CharField(blank=True, max_length=100, verbose_name='posição da assinatura'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='suporte',
            field=models.CharField(blank=True, max_length=100, verbose_name='Suporte'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='tecnica',
            field=models.CharField(blank=True, max_length=100, verbose_name='Técnica'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='ultimo_valor_estimado',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8, verbose_name='Último Valor Estimado (R$)'),
        ),
        migrations.AlterField(
            model_name='materiais',
            name='valor_estimado_original',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8, verbose_name='Valor Estimado Original (R$)'),
        ),
    ]
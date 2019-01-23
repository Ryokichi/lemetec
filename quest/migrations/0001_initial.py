# Generated by Django 2.1.4 on 2019-01-20 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('img_nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('qtd_respondida', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('pergunta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Pergunta')),
            ],
        ),
        migrations.AddField(
            model_name='pergunta',
            name='questionario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quest.Questionario'),
        ),
    ]
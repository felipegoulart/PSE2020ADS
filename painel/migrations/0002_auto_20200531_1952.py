# Generated by Django 3.0.6 on 2020-05-31 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivos',
            name='arquivos',
            field=models.FileField(upload_to=''),
        ),
    ]
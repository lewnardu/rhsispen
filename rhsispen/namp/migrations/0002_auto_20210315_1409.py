# Generated by Django 3.1.7 on 2021-03-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('namp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enderecosetor',
            name='municipio',
            field=models.CharField(default='Não registrado', max_length=100),
        ),
    ]
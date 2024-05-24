# Generated by Django 5.0.6 on 2024-05-24 06:41

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_typeurl_project_type_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('color', colorfield.fields.ColorField(choices=[('#FFFFFF', 'bílá'), ('#000000', 'černá'), ('#FF0000', 'červená'), ('#00FF00', 'zelená'), ('#0000FF', 'modrá'), ('#FFFF00', 'žlutá')], default='#FFFFFF', image_field=None, max_length=25, samples=None)),
            ],
        ),
    ]

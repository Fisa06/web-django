# Generated by Django 5.0.6 on 2024-05-24 06:15

import django.db.models.deletion
from django.db import migrations, models

def insert_types(apps, schema_editor):
    TypeUrl = apps.get_model('portfolio', 'TypeUrl')
    TypeUrl.objects.create(name='Github', icon='static/images/icons/github.png')
    TypeUrl.objects.create(name='Gitlab', icon='static/images/icons/gitlab.png')


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20240522_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('icon', models.ImageField(upload_to='static/images/icons/', verbose_name='Icon')),
            ],
        ),
        migrations.RunPython(insert_types),
        migrations.AddField(
            model_name='project',
            name='type_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='projects', to='portfolio.typeurl'),
        ),
    ]

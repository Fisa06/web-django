# Generated by Django 5.0.6 on 2024-05-22 11:10

from django.db import migrations, models

def insert_types(apps, schema_editor):
    TypeProject = apps.get_model('portfolio', 'TypeProject')
    TypeProject.objects.create(name='Osobní')
    TypeProject.objects.create(name='Školní')


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_project_created_at_project_modified_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeProject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RunPython(insert_types),
    ]
# Generated by Django 5.0.6 on 2024-05-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Project Description'),
        ),
    ]

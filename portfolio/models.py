from django.db import models

# Create your models here.


class TypeProject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Name',
                            unique=True)
    description = models.TextField(max_length=1000,null=True, blank=True)


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Project Name')
    description = models.TextField(max_length=1000,
                                   verbose_name='Project Description',
                                   blank=True, null=True)
    logo = models.ImageField(upload_to='static/images/',
                             verbose_name='Project Logo')

    url = models.URLField(max_length=200,
                          verbose_name='Project URL',
                          blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    type = models.ForeignKey('TypeProject', on_delete=models.RESTRICT,
                             related_name='projects', default=1)


    class Meta:
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekty'

    def __str__(self):
        return f"{self.name}"
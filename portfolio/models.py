from colorfield.fields import ColorField
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from portfolio.managers import ProjectManager


# Create your models here.


class TypeProject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Name',
                            unique=True)
    description = models.TextField(max_length=1000,null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Typ Projektu'
        verbose_name_plural = 'Typy Projektu'

class TypeUrl(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                             verbose_name='Name',
                             unique=True)
    icon = models.ImageField(upload_to='static/images/icons/', verbose_name='Icon')

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Typ URL'
        verbose_name_plural = 'Typy URL'


class TypeTag(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "bílá",),
        ("#000000", "černá",),
        ("#FF0000", "červená",),
        ("#00FF00", "zelená",),
        ("#0000FF", "modrá",),
        ("#FFFF00", "žlutá",)
    ]
    DEFAULT_COLOR = "#FFFFFF"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Name',
                            unique=True)
    color = ColorField(default=DEFAULT_COLOR,
                       samples=COLOR_PALETTE)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tagy'

    def __str__(self):
        return f"{self.name} - {self.color}"

class Project(models.Model):

    objects = ProjectManager()

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            verbose_name='Project Name')
    description = MarkdownxField(max_length=5000, blank=True, null=True,
                                 verbose_name='Project Description')
    logo = models.ImageField(upload_to='static/images/',
                             verbose_name='Project Logo')

    url = models.URLField(max_length=200,
                          verbose_name='Project URL',
                          blank=True, null=True)

    type_url = models.ForeignKey('TypeUrl', on_delete=models.RESTRICT,
                                 related_name='projects', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    type = models.ForeignKey('TypeProject', on_delete=models.RESTRICT,
                             related_name='projects', default=1)

    tags = models.ManyToManyField('TypeTag', related_name='projects', blank=True
                                  , verbose_name='Tagy')

    @property
    def get_pretty_description(self):
        from markdownx.utils import markdownify
        return markdownify(self.description)


    class Meta:
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekty'

    def __str__(self):
        return f"{self.name}"
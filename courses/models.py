from django.db import models

# Create your models here.

modal_choices = (
    ('B', 'Bacharelado'),
    ('L', 'Licenciatura'),
    ('PS', 'Pós-Graduação Mestrado'),
    ('PD', 'Pós-Graduação Doutorado'),
    ('PP', 'Pós-Graduação Pós-Doutorado'),
    ('PL', 'Pós-Graduação Lato Sensu'),
    ('TL', 'Tecnólogo'),
    ('T', 'Técnico'),
)

class Institute(models.Model):
    username = models.CharField('Sigla da Unidade de Ensino', max_length=15)
    name = models.CharField('Nome da Unidade de Ensino', max_length=100)

    class Meta:
        verbose_name = 'Unidade de Ensino'
        verbose_name_plural = 'Unidades de Ensino'

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField('Curso', max_length=30)
    modal = models.CharField('Modalidade', max_length=10, choices=modal_choices, default='L')
    institute = models.ForeignKey(Institute, verbose_name='Unidade de Ensino', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return "{} - {} ({})".format(self.name, self.modal, self.institute.username)

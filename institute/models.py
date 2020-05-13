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
    """
        Institutos que tem ou terá relacao com o Congresso, seja para sediar ou para compor instituicoes onde
        inscritos pertencem.
    """
    username = models.CharField('Sigla', max_length=15)
    name = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'

    def __str__(self):
        return self.name

class Courses(models.Model):
    """
        Cursos que tem relacao com o congresso, seja para atualizar como compor curso onde
        inscritos pertencem.
    """
    name = models.CharField('Curso', max_length=30)
    modal = models.CharField('Modalidade', max_length=10, choices=modal_choices, default='L')
    institute = models.ForeignKey(Institute, verbose_name='Instituição', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def get_readable_choices(self):
        return dict(modal_choices)[self.modal]

    def __str__(self):
        return "{} - {} ({})".format(self.name, self.modal, self.institute.username)

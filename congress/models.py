import os
import uuid

from PIL import Image

from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html

from core.utils import UploadToPathAndRename

# Create your models here.
Users = get_user_model()

class TypeCongress(models.Model):
    """
        Armazena tipo de congressos, exemplo: Colóquio, Simpósios, Semana de Estudos, entre outros
    """
    type_congress = models.CharField('Tipo de Congresso', max_length=50)

    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipos de Evento'

    def __str__(self):
        return self.type_congress

class Congress(models.Model):
    """
        Dados essenciais dos Congressos
    """
    username = models.CharField('Apelido do evento', max_length=20, blank=True, null=True)
    slug = models.SlugField('Referencia', max_length=100, blank=True, null=True, default="")
    name = models.CharField('Nome do Evento', max_length=100)
    type_congress = models.ForeignKey(TypeCongress, verbose_name='Tipo do evento', on_delete=models.CASCADE)
    date_start_subscription = models.DateTimeField("Iniciar Inscrições", auto_now=False, auto_now_add=False, default=timezone.now)
    date_start = models.DateTimeField("Primeiro dia", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close_subscription = models.DateTimeField("Encerrar Recebimento de Inscrições", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close = models.DateTimeField("Finalização do evento", auto_now=False, auto_now_add=False, default=timezone.now)
    date_close_awards = models.DateTimeField("Finalizar Inscrições com Premiação", auto_now=False, auto_now_add=False, default=timezone.now)
    workload = models.DecimalField('Carga horária', max_digits=4, decimal_places=2, default=1, help_text='Em horas')
    is_closed = models.BooleanField('Está fechado?', default=False)

    class Meta:
        verbose_name = 'Congresso'
        verbose_name_plural = 'Congressos'
        ordering = ['name', '-date_start']

    def __str__(self):
        return self.name

    def get_date(self):
        return "{}".format(self.date_start.strftime("%m/%Y"))
    get_date.short_description = 'Data'

    def get_pdf_url(self):
        return format_html("<a href={}>pdf</a>".format(reverse('congress:report_list_pdf', kwargs={'slug': self.slug})))
    get_pdf_url.short_description = 'Lista Presenca'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify("{} {}".format(self.name, self.date_start.strftime("%Y")))

        return super().save(*args, **kwargs)

class Subscriptions(models.Model):
    """
        Inscritos
    """
    congress = models.ForeignKey(Congress, verbose_name='Congresso', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name='Usuario inscrito', on_delete=models.CASCADE)
    is_adm = models.BooleanField('Administrador do Evento', default=False)
    is_staff = models.BooleanField('Monitor', default=False)
    is_payment = models.BooleanField('Pagamento', default=False)

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return "{}".format(self.user.name)

    def get_congress_info(self):
        return "{} ({})".format(self.congress.name, self.congress.date_start.strftime("%Y"))
    get_congress_info.short_description = "Evento"

class CertificateImages(models.Model):
    """
        Imagem de Fundo para certificados
    """
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)
    image = models.ImageField("Certificado", default="certificate.png", upload_to=UploadToPathAndRename('certificates/'))

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return "{} ({})".format(self.congress.username, self.congress.date_start.strftime("%m/%Y"))

    def save(self, *args, **kwargs):
        img_cert = Image.open(self.certificate.path)

        if img_cert.height != 2480 or img_cert.width != 3508:
            output_size = (2480, 3508)
            img_cert.thumbnail(output_size)
            img_cert.save(self.certificate.path)

        super().save(*args, **kwargs)

class InstituteImages(models.Model):
    """

    """
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)
    image = models.ImageField("Instituto", default="default.png", upload_to=UploadToPathAndRename('institute/'))

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return "{} ({})".format(self.congress.username, self.congress.date_start.strftime("%m/%Y"))

    def get_detail_url(self):
        return reverse("core:images_detail", kwargs={'pk': self.pk})

class LogoImages(models.Model):
    """
        Imagem de Logo, Fundo de Cetificado e Logo de Instituicao
    """
    congress = models.OneToOneField(Congress, on_delete=models.CASCADE)
    image = models.ImageField("Logo", default="default.png", upload_to=UploadToPathAndRename('logo/'))


    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return "{} ({})".format(self.congress.username, self.congress.date_start.strftime("%m/%Y"))

    def get_detail_url(self):
        return reverse("core:images_detail", kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        img_logo = Image.open(self.logo.path)

        if img_logo.height > 300 or img_logo.width > 300:
            output_size = (300,300)
            img_logo.thumbnail(output_size)
            img_logo.save(self.logo.path)

        super().save(*args, **kwargs)

class LuckyNumber(models.Model):
    """
        Numero para eventuais sorteios
    """
    congress = models.ForeignKey(Congress, verbose_name='Evento', on_delete=models.CASCADE)
    user = models.ForeignKey(Users, verbose_name="Usuario", on_delete=models.CASCADE)
    number = models.CharField("Numero da sorte", max_length=3)

    class Meta:
        verbose_name = "Numero da Sorte"
        verbose_name_plural = "Sorteios"

    def __str__(self):
        return "({}) {}".format(self.congress, self.user)

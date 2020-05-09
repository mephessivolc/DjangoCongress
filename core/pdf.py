import os
import io

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic

from reportlab.lib import colors, utils
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (getSampleStyleSheet, ParagraphStyle,
        TA_CENTER, TA_LEFT
    )
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import (Paragraph, Table, TableStyle, SimpleDocTemplate,
        Spacer, Frame, Image, PageTemplate, KeepInFrame
    )

########################################################################

def get_image(path, width=10, height=10, unit=mm):
    """
        Mantem aspectRatio da imagem
    """
    img = utils.ImageReader(path)
    iw, ih = img.getSize()

    aspect = ih/float(iw)
    nWidth = width * unit
    nHeight = aspect * width * unit

    if nHeight > height * unit:
        aspect = iw/float(ih)
        nWidth = aspect * height * unit
        nHeight = height * unit

    return Image(path, width=nWidth, height=nHeight)

class PdfManager(generic.TemplateView):
    title = "Title"
    subtitle = "Subtitle"
    filename = 'Default'
    doc_name = 'default'
    extra_lines = 0
    congress_queryset = None
    list_queryset = None
    date = timezone.now()
    pdf_path = None

    def __init__(self, **kwargs):
        # self.path_logo_congress = path_logo_congress
        # self.path_logo_institute = path_logo_institute

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.width, self.height = A4
        self.styles = getSampleStyleSheet()
        self.styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
        self.kwargs = kwargs

    def get_doc_name(self):
        """
            Return the name of pdf
        """
        return "{}.pdf".format(self.doc_name)

    def get_pdf_path(self):
        """
            Return files path to create the pdf
        """
        if self.pdf_path is None:
            pdf_path = settings.PDF_PATH

            if not pdf_path:
                pdf_path = settings.STATIC_ROOT

        pdf_path = os.path.join(pdf_path, 'tmp')

        return pdf_path

    def get_full_path(self):
        """
            Return the full path of pdf document
        """
        full_path = "{}/{}.pdf".format(self.get_pdf_path(), self.doc_name)

        return full_path

    def get_congress_queryset(self):
        if self.congress_queryset is None:
            raise ImproperlyConfigured(
                "PdfManager requires either a definition of "
                "'data_congress' or an implementation of 'get_path_logo_congress()'"
            )
        return self.congress_queryset

    def get_path_logo_congress(self):
        return self.get_congress_queryset().images.logo.path

    def get_path_institute_congress(self):
        return self.get_congress_queryset().images.institute.path

    def coord(self, x, y, unit=1):
        """
            Classe ajudante para auxiliar o posicionamento de objetos Canvas fluidos
        """
        x, y = x * unit, self.height - y * unit
        return x,y

class PagePdfManager(PdfManager):

    def createHeader(self, canvas, doc):
        """
            Criando o Primeira pagina do Documento
        """
        self.c = canvas
        normal = self.styles["Normal"]
        center = self.styles['Center']

        imgLeft = get_image(self.get_path_institute_congress(), height=100)
        imgLeft._restrictSize(40*mm, 20*mm)
        frameLeft = Frame(
            *self.coord(10*mm, 30*mm),
            50*mm,
            20*mm,
        )
        ldata = [imgLeft]

        frameLeft.addFromList(ldata, self.c)

        frameCenter = Frame(
            *self.coord(60*mm, 30*mm),
            90*mm,
            20*mm,
        )

        title_header_text = "<strong>{}</strong>".format(self.title)
        subtitle_header_text = "{}".format(self.subtitle)
        ptitle = KeepInFrame(85*mm, 15*mm, [Paragraph(title_header_text, center)])
        psubtitle = KeepInFrame(85*mm, 10*mm, [Paragraph(subtitle_header_text, center)])

        mdata  = [ptitle, psubtitle]

        frameCenter.addFromList(mdata, self.c)

        imgRight = get_image(self.get_path_logo_congress(), width=100)
        imgRight._restrictSize(40*mm, 20*mm)
        frameRight = Frame(
            *self.coord(150*mm, 30*mm),
            50*mm,
            20*mm,
        )

        rdata=[imgRight]
        frameRight.addFromList(rdata, self.c)

        date_header_text = "<font size='6'>Data: {}</font>".format(self.date.strftime("%d/%m/%Y"))
        pdata = Paragraph(date_header_text, normal)
        pdata.wrapOn(self.c, self.width, self.height)
        pdata.drawOn(self.c, *self.coord(self.width-30*mm, 38*mm))

        self.addPageNumber(canvas, doc)

    def addPageNumber(self, canvas, doc):
        """
        Add the page number
        """
        self.c = canvas
        center = self.styles["Center"]
        page_num = canvas.getPageNumber()
        text = "<font size='8'>{}</font>".format(page_num)

        page = Paragraph(text, center)
        page.wrapOn(self.c, self.width, self.height)
        page.drawOn(self.c, 0.5, 15 * mm)

class TablePdfManager(PagePdfManager):

    def builder(self):
        buffer = io.BytesIO()

        self.doc = SimpleDocTemplate(self.get_full_path())
        self.story = [Spacer(0, 15 * mm)]
        self.createLineItems()

        self.doc.build(self.story, onFirstPage=self.createHeader,
                onLaterPages=self.addPageNumber
            )

    def createLineItems(self):
        """
        Criando as linhas de itens
        """

        text_data = [
        "",
        "Nome",
        "Assinatura",
        ]

        d = []

        font_size = 11
        centered = ParagraphStyle(name='centered', alignment=TA_CENTER)
        flushleft = ParagraphStyle(name='left', alignment=TA_LEFT)

        # first line
        for text in text_data:
            ptext = "<font size='{}'><strong>{}</strong></font>".format(font_size, text)
            p = Paragraph(ptext, centered)
            d.append(p)

            data = [d]
            line_num = 1

            formatted_line_data = []

            for obj in self.data_list:
                line_data = [
                Paragraph("<font size='{}'>{}</font>".format(font_size-2, line_num),
                centered),
                Paragraph("<font size='{}'>{}</font>".format(font_size-2, obj.name.upper()),
                flushleft),
                Paragraph("<font size='{}'>{}</font>".format(font_size-2, ""),
                centered),
                ]

                data.append(line_data)
                formatted_line_data = []
                line_num = line_num + 1

        for i in range(self.extra_lines):
            data.append([
                Paragraph("<font size='{}'>{}</font>".format(font_size-2, line_num),
                centered),
                '',
                ''])
            line_num = line_num + 1

        table_style = TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ])

        table = Table(data, colWidths=[10.5*mm, 85*mm, 95*mm])
        table.setStyle(table_style)

        data_len = len(data)
        for each in range(1, data_len):
            bg_color = colors.white
            if each % 2 == 0:
                bg_color = colors.whitesmoke

        table.setStyle(TableStyle([("BACKGROUND", (0,each), (-1,each), bg_color)]))

        self.story.append(table)

    def render_to_response(self, context, **response_kwargs):
        """
            Executar a construção do arquivo pdf
        """
        self.builder()

        fs = FileSystemStorage(self.get_pdf_path())
        with fs.open(self.get_doc_name()) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(self.filename)

            return response

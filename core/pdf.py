from io import BytesIO

from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.template.loader import get_template, render_to_string

from pylatex import (
        Document, LongTabu, MultiColumn, Center, NoEscape,
        StandAloneGraphic, Table, FlushRight, FootnoteText,
        MultiRow,
    )

from pylatex.utils import bold

class PdfManager():
    def __init__(self, **kwargs):
        self.context = self.get_context(**kwargs)

    def get_context(self, **kwargs):
        context = kwargs
        if 'path' not in context:
            context['path'] = "{}/default".format(settings.PDF_PATH)

        if 'full_path' not in context:
            context['full_path'] = "{}.pdf".format(context['path'])

        if 'extra_lines' not in context:
            context['extra_lines'] = 0

        if 'data' not in context:
            context['data'] = []

        if 'filename' not in context:
            context['filename'] = 'default'

        if 'image_logo' not in context:
            context['image_logo'] = "{}/default.png".format(settings.MEDIA_ROOT)

        if 'image_institution' not in context:
            context['image_institution'] = "{}/logo_site.png".format(settings.MEDIA_ROOT)

        return context

    def render_to_file(self):
        geometry_options = {
                "tmargin": "1cm",
                "lmargin": "1cm",
                "rmargin": "1cm",
                "bmargin": "1cm",
            }
        pdf = Document(self.context['path'],
            page_numbers=True,
            geometry_options=geometry_options)

        with pdf.create(LongTabu("cX[c]c",)) as data_table:
            data = [
                StandAloneGraphic(self.context['image_logo'],
                    image_options=[NoEscape(r'width=50px'), 'keepaspectratio']),
                'Texto',
                StandAloneGraphic(self.context['image_institution'],
                    image_options=[NoEscape(r'width=50px'), 'keepaspectratio']),
            ]
            data_table.add_row(data)
            data_table.add_row("", 'Padraozinho', "")
            data_table.add_hline()

        with pdf.create(FlushRight()) as data:
            data.append(FootnoteText('data: 01/01/2020'))

        with pdf.create(LongTabu("|c|X[l]|X[l]|")) as data_table:
            data_table.add_hline()
            data_table.add_row([
                        "",
                        'Nome',
                        'Assinatura',
                    ],
                    mapper=[bold]
                )

            data_table.add_hline()
            data_table.end_table_header()
            data_table.add_hline()
            data_table.add_hline()
            cont = 1

            for i in self.context['data']:
                data_table.add_row(["{}".format(cont), i.name, ""])
                data_table.add_hline()
                cont = cont + 1

            for i in range(self.context['extra_lines']):
                data_table.add_row(["{}".format(cont), "", ""])
                data_table.add_hline()
                cont = cont + 1

        pdf.generate_pdf()

        if not self.context['full_path']:
            return HttpResponseNotFound('Arquivo não encontrao')

        return self.context['full_path']

class ListRender(PdfManager):

    def render_to_response(self):

        response = FileResponse(open(self.render_to_file(), 'rb'))

        # response = HttpResponse(path)
        response['Content_Type'] = 'application/pdf'
        response['Content-Disposition'] = 'inline; filename={}.pdf'.format(self.context['filename'])

        return response

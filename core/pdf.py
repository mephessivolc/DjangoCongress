from io import BytesIO

from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.template.loader import get_template, render_to_string

from pylatex import Document, LongTabu, MultiColumn, Center, NoEscape
from pylatex.utils import bold

class Render():

    def __init__(self, context):
        self.context = context

    def render_to_response(self):
        geometry_options = {
                "tmargin": "1cm",
                "lmargin": "1cm",
                "rmargin": "1cm",
                "bmargin": "1cm",
                "includeheadfoot": True
            }
        pdf = Document(settings.PDF_PATH, page_numbers=True, geometry_options=geometry_options)

        with pdf.create(LongTabu("|c|X[l]|X[l]|")) as data_table:
            data_table.add_hline()
            data_table.add_row([
                        "#",
                        "Nome",
                        "Assinatura",
                    ],
                    mapper=[bold]
                )
            data_table.add_hline()
            data_table.end_table_header()
            data_table.add_hline()
            data_table.add_hline()
            cont = 1
    
            for i in self.context['form']:
                data_table.add_row(["{}".format(cont), i.name, ""])
                data_table.add_hline()
                cont = cont + 1

        pdf.generate_pdf()
        filename = "{}.pdf".format(self.context['filename'] or 'default')

        path = "{}.pdf".format(settings.PDF_PATH)
        if not path:
            return HttpResponseNotFound('Arquivo não encontrao')

        response = FileResponse(open(path, 'rb'))

        # response = HttpResponse(path)
        response['Content_Type'] = 'application/pdf'
        response['Content-Disposition'] = 'inline; filename={}'.format(filename)

        return response

import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template import Context, loader
from django.template.loader import render_to_string, get_template

from pylatex import (
    Document, Section, Subsection,
    Command, UnsafeCommand, LongTable,
    MultiColumn, TextColor, LineBreak
)
from pylatex.package import Package
from pylatex.utils import bold, italic, NoEscape
from pylatex.basic import LargeText
from pylatex.position import FlushRight, Center, VerticalSpace


path_pdf = os.path.join(settings.STATIC_ROOT, 'pdf/')

class ReportListUsersPDF(Document):

    def __init__(self, **kwargs):
        geometry_options = {
            "left": "0.5cm",
            "right": "0.5cm",
            "top": "2cm",
            "bottom": "2cm",
        }

        super().__init__(
            geometry_options=geometry_options,
            default_filepath=path_pdf+'base',
            document_options='11pt',
            page_numbers=True,
        )

        self.add_color(name="lightgray", model="gray", description="0.95")
        self.add_color(name="middlegray", model="gray", description="0.70")

        self.name = kwargs.get('pdf_name')
        self.query = kwargs.get('query')
        self.title_page = kwargs.get('title_page')
        self.sub_title_page = kwargs.get('sub_title')

    def set_title_page(self, title):
        self.title_page = title

    def get_title_page(self):
        return self.title_page or 'Lista de Presença'

    def set_sub_title_page(self, title):
        self.sub_title_page = title

    def get_sub_title_page(self):
        return self.sub_title_page or ''

    def set_pdf_name(self, name):
        self.name = name

    def get_pdf_name(self):
        return self.name or 'Users'

    def set_query(self, query):
        self.query = query

    def get_query(self):
        return self.query

    def create_header(self):
        self.append(self.get_title_page())
        self.append('\n')
        self.append(self.get_sub_title_page())

    def get_pdf(self):
        self.generate_pdf()
        fs = FileSystemStorage(path_pdf)

        with fs.open("base.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="{}.pdf"'.format(self.get_pdf_name()) # para exibir em nova aba

            return response

    def get_document(self):
        self.create_header()
        with self.create(LongTable("|c|p{9cm}|p{9cm}|")) as data_table:
            data_table.add_hline()
            data_table.add_row([
                "",
                MultiColumn(1, align='c|',
                    data=bold('NOME')),
                MultiColumn(1, align='c|',
                    data=bold("ASSINATURA"))
            ], color='middlegray')
            data_table.end_table_header()
            data_table.add_hline()
            data_table.end_table_footer()
            data_table.add_hline()
            data_table.end_table_last_footer()
            count = 1
            for row in self.get_query():
                data_table.add_hline()
                if count % 2 == 0:
                    data_table.add_row([count, row.name, ""], color='lightgray')
                else:
                    data_table.add_row([count, row.name, ""],)
                count += 1

        return self.get_pdf()

class ReportListUsersEmailPDF(ReportListUsersPDF):

    def get_document(self):
        self.create_header()

        with self.create(LongTable("|c|p{9cm}|p{9cm}|")) as data_table:
            data_table.add_hline()
            data_table.add_row([
                "",
                MultiColumn(1, align='c|',
                    data=bold('NOME')),
                MultiColumn(1, align='c|',
                    data=bold("E-Mail"))
            ], color='middlegray')
            data_table.end_table_header()
            data_table.add_hline()
            data_table.end_table_footer()
            data_table.add_hline()
            data_table.end_table_last_footer()
            count = 1
            for row in self.get_query():
                data_table.add_hline()
                data_table.add_row([count, row.name, row.email])
                count += 1

        return self.get_pdf()

import csv

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export CSV Selected"


class ExportPdfMixin:
    def export_as_pdf(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        rows = []
        for obj in queryset:
            values = [getattr(getattr(obj, field), 'name', getattr(obj, field)) for field in field_names]
            rows.append(values)

        html_string = render_to_string('pdf_template.html',
                                       {'hcolumns': field_names, 'meta': meta.app_label,
                                        'rows': rows})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(meta.app_label))
        fs = FileSystemStorage('/tmp')
        with fs.open("{}.pdf".format(meta.app_label)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(meta.app_label)
        return response

    export_as_pdf.short_description = "Export PDF Selected"

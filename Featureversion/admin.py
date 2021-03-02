from django.contrib import admin
from django.utils.html import format_html
from django_admin_search.admin import AdvancedSearchAdmin

from clair.export import ExportCsvMixin, ExportPdfMixin
from .forms import FeatureVersionSearchForm
from .models import Featureversion


# Register your models here.


def feature_link(self):
    return format_html(
        '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
            app_name=self.feature._meta.app_label, db_table=self.feature._meta.db_table,
            db_table_primary_key=self.feature.id, db_table_field=self.feature.name))


feature_link.short_description = "Feature Name"
feature_link.admin_order_field = "feature"


def namespace_link(self):
    return format_html(
        '<a href="/{app_name}/{db_table}/{db_table_primary_key}/change/">{db_table_field}</a>'.format(
            app_name=self.feature.namespace._meta.app_label, db_table=self.feature.namespace._meta.db_table,
            db_table_primary_key=self.feature.namespace.id, db_table_field=self.feature.namespace.name))


namespace_link.short_description = "Namespace Name"
namespace_link.admin_order_field = "feature__namespace__name"


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(Featureversion)
class FeatureversionAdmin(AdvancedSearchAdmin, ExportCsvMixin, ExportPdfMixin):
    list_display = ("id", feature_link, "version", namespace_link)
    raw_id_fields = ("feature",)
    search_fields = ("id", "feature__name", "version", "id")
    ordering = ("version", "id")
    list_per_page = 20
    list_filter = (('version', custom_titled_filter("Feature Version")),
                   ('feature__namespace__name', custom_titled_filter("Namespace")))
    list_display_links = (feature_link, "version", "id", namespace_link)
    actions = ["export_as_csv", "export_as_pdf"]
    search_form = FeatureVersionSearchForm

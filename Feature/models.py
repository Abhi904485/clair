from django.db import models
from django.utils.html import format_html

from Namespace.models import Namespace


# Create your models here.


class Feature(models.Model):
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Feature Name", max_length=128)

    class Meta:
        managed = True
        db_table = 'feature'
        unique_together = (('namespace', 'name'),)

    def __str__(self):
        return self.name

    # def get_vulnerability_fixedin_feature_version(self):
    #     from VulnerabilityFixedinFeature.models import VulnerabilityFixedinFeature
    #     vulnerability_fixedin_feature_version = VulnerabilityFixedinFeature.objects.filter(feature__name=self.name)
    #     result = "  \t\n".join([vffv.version for vffv in vulnerability_fixedin_feature_version])
    #     return result

    # def get_vulnerability_fixedin_feature_version(self):
    #     from VulnerabilityFixedinFeature.models import VulnerabilityFixedinFeature
    #     vulnerability_fixedin_feature_version = VulnerabilityFixedinFeature.objects.filter(feature__name=self.name)
    #     options = ""
    #     for vffv in vulnerability_fixedin_feature_version:
    #         options += '<option value="{}">{}</option>\n'.format(vffv.version, vffv.version)
    #     select = '<select name="vulnerability_fixedin_feature_version" id="#">{}</select>'.format(options)
    #     return format_html(select)

    # def get_vulnerability_fixedin_feature_version(self):
    #     from VulnerabilityFixedinFeature.models import VulnerabilityFixedinFeature
    #     vulnerability_fixedin_feature_version = VulnerabilityFixedinFeature.objects.filter(feature__name=self.name)
    #     options = ""
    #     for vffv in vulnerability_fixedin_feature_version:
    #         options += '<li>{}</li>\n'.format(vffv.version)
    #     select = '<ul>{}</ul>'.format(options)
    #     return format_html(select)

    def get_vulnerability_fixedin_feature_version(self):
        from VulnerabilityFixedinFeature.models import VulnerabilityFixedinFeature
        vulnerability_fixedin_feature_version = VulnerabilityFixedinFeature.objects.filter(feature__name=self.name)
        options = ""
        for vffv in vulnerability_fixedin_feature_version:
            options += '{}\t'.format(vffv.version)
        if len(options) == 0:
            textarea = "<p>-</p>".format(options)
        else:
            textarea = "<textarea class='vLargeTextField' rows='2' cols='10'>{}</textarea>".format(options)
        return format_html(textarea)

    get_vulnerability_fixedin_feature_version.short_description = "Vulnerability Fixed In Feature Version"
    # get_vulnerability_fixedin_feature_version.admin_order_field = "featureversion"

    def get_vulnerability_link(self):
        from Vulnerability.models import Vulnerability
        vulnerability = Vulnerability.objects.filter(namespace__name=self.namespace.name).values_list('name', flat=True).order_by('name')
        options = ""
        for vul in vulnerability:
            options += '{}\t'.format(vul)
        textarea = "<textarea class='vLargeTextField' rows='2' cols='10'>{}</textarea>".format(options)
        return format_html(textarea)

    get_vulnerability_link.short_description = "Vulnerability NAME"
    # get_vulnerability_link.admin_order_field = "vulnerabilityfixedinfeature__vulnerability__name"

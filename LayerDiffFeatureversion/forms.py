from django.forms import CharField, TextInput, IntegerField, forms

from .models import LayerDiffFeatureversion


class LayerDiffFeatureVersionForm(forms.Form):
    id = IntegerField(label="Search By LDFV ID", required=False, widget=TextInput(
        attrs={
            'filter_field': 'id',
            'filter_method': '__exact',
            'placeholder': "1",
        }
    ))
    name = CharField(label="Search By Layer Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'layer__name',
            'filter_method': '__exact',
            'placeholder': "84c5f6e03bf04e139705ceb2612ae274aad94f8dcf8cc630fbf6d91975f2e1c9d121f8d1c4128ebc1e95e5bfad90a0189b84eadbbb2fbaad20cbb26d20b2c8a2",
            'size': '150',
        }
    ))

    namespace_name = CharField(label="Search By Namespace name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'layer__namespace__name',
            'filter_method': '__exact',
            'placeholder': "alpine:2.1.4",
        }
    ))

    modification = CharField(label="Search By Modification", required=False, widget=TextInput(
        attrs={
            'filter_field': 'modification',
            'filter_method': '__exact',
            'placeholder': "add or delete",
        }
    ))

    feature_version = CharField(label="Search By Feature Version Name", required=False, widget=TextInput(
        attrs={
            'filter_field': 'featureversion__version',
            'filter_method': '__exact',
            'placeholder': "5.0-4",
        }
    ))

    class Meta:
        model = LayerDiffFeatureversion
        fields = '__all__'
        model._meta.fields[0].verbose_name = "LayerDiff Feature Version ID"

from django.forms import BooleanField, ModelForm

from blog.models import Article


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fiеld_name, fiеld in self.fields.items():
            if isinstance(fiеld, BooleanField):
                fiеld.widget.attrs["class"] = "form-check-input"
            else:
                fiеld.widget.attrs["class"] = "form-control"


class ArticleForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Article
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'

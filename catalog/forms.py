from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fiеld_name, fiеld in self.fields.items():
            if isinstance(fiеld, BooleanField):
                fiеld.widget.attrs["class"] = "form-check-input"
            else:
                fiеld.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    FORBIDDEN_WORDS = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар'
    ]
    class Meta:
        model = Product
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'

    def clean_product_name(self):
        """Валидация названия продукта"""
        product_name = self.cleaned_data.get('product_name')
        return self._validate_forbidden_words(field_name='product_name', value=product_name)

    def clean_description(self):
        """Валидация описания продукта"""
        description = self.cleaned_data.get('description')
        return self._validate_forbidden_words(field_name='description', value=description)

    def clean_price(self):
        """Валидация цены"""
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def _validate_forbidden_words(self, field_name, value):
        """
        Внутренний метод для проверки на запрещенные слова
        """
        # приводим к нижнему регистру
        value_lower = value.lower()

        # Проверяем каждое запрещенное слово
        for word in self.FORBIDDEN_WORDS:
            if word in value_lower:
                # Формируем сообщение об ошибке с выделением слова
                error_message = (
                    f"Содержимое содержит запрещенное слово: '{word}'. "
                    "Пожалуйста, измените текст."
                )
                raise ValidationError(error_message, code='forbidden_word')

        return value


class CategoryForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        # exclude = ('created_at', 'updated_at')
        fields = '__all__'

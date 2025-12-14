from django import forms
from .models import Order


class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Поиск'}))


class OrderModelForm(forms.ModelForm):
    DELIVERY_CHOICES = ((0, 'Выберите, пожалуйста'), (1, 'Доставка'), (2, 'Самовывоз'))
    delivery = forms.TypedChoiceField(
        label='доставка', choices=DELIVERY_CHOICES, coerce=int
    )

    class Meta:
        model = Order
        exclude = ['discount', 'status', 'need_delivery']
        labels = {
            'adress': 'Полный адрес (Страна, город, индекс, улица, дом, квартира)'
        }

        widgets = {
            'adress': forms.Textarea(
                attrs={
                    'cols': 80,
                    'rows': 6,
                    'placeholder': 'При самовывозе можно оставить это поле пустым',
                }
            ),
            'notice': forms.Textarea(attrs={'cols': 80, 'rows': 6}),
        }

    def clean_delivery(self):
        data = self.cleaned_data['delivery']

        if data not in (1, 2):
            raise forms.ValidationError('Небходимо указать способ доставки')

        return data

    def clean(self):
        delivery = self.cleaned_data['delivery']
        adress = self.cleaned_data['adress']

        if delivery == 1 and not adress:
            raise forms.ValidationError('Укажите адрес доставки')

        return self.cleaned_data

from django import forms
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(attrs={'palaceholder': 'Введите строку поиска...'})
    )


# <input type="text" value="Введите строку поиска..." onfocus="this.value='';" onblur="if (this.value == '') {this.value ='';}">


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date', 'status_feed_back']

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'title': forms.TextInput(attrs={'placeholder': 'Тема'}),
            'content': forms.Textarea(attrs={'placeholder': 'Сообщение'}),
        }


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')

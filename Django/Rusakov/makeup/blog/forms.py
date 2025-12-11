from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={'palaceholder': 'Введите строку поиска...'}))
	# <input type="text" value="Введите строку поиска..." onfocus="this.value='';" onblur="if (this.value == '') {this.value ='';}">
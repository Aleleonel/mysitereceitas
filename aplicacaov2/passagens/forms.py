from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .class_viagem import tipos_de_classe


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    datapesquisa = forms.DateField(
        label='Data da Pesquisa', disabled=True, initial=datetime.today)
    class_viagem = forms.ChoiceField(
        label='classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=150)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida:Não incluir números')
        else:
            return origem

    def clean_destino(self):
        destino = self.cleaned_data.get('destino')
        if any(char.isdigit() for char in destino):
            raise forms.ValidationError('Destino inválida:Não incluir números')
        else:
            return destino

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        if origem == destino:
            self.add_error('destino', 'Origem e Destino não pode ser iguais')
        return self.cleaned_data

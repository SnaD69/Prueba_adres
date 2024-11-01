from django import forms

class CSVUploadForm(forms.Form):
    archivo_csv = forms.FileField(label='Seleccionar archivo CSV')

class TextUploadForm(forms.Form):
    archivo_txt = forms.FileField(label='Seleccionar archivo de texto')
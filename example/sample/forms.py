# -*- coding: utf-8 -*-
from django import forms

from masked_forms.forms import MaskedWidget

class SampleForm(forms.Form):
    telefone = forms.CharField(widget=MaskedWidget(mask_format='(99) 9999-9999'))
    cpf      = forms.CharField(widget=MaskedWidget(mask_format='999.999.999-99'))
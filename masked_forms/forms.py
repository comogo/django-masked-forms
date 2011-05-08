# -*- coding: utf-8 -*-
from django.forms import TextInput

class MaskedWidget(TextInput):
    """
    jQuery MaskedInput Widget.
    """
    class Media:
        js = (
            'masked_forms/js/jquery.maskedinput.js',
            'masked_forms/js/masked_forms.js',
        )
    def __init__(self, mask_format=None, *args, **kwargs):
        super(MaskedWidget, self).__init__(*args, **kwargs)
        if not mask_format:
            raise TypeError("mask_format paramater can't by empty" )
        self.mask_format = mask_format
        self.attrs['class'] = ' masked'
        self.attrs['mask']  = self.mask_format 
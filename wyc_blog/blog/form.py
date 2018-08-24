#!/usr/bin/python
# -*- coding: utf-8 -*-


from django import forms
from blog import models


class Class_Text(forms.Form):
    shop_type_quere = forms.ChoiceField(label=u'', widget=forms.widgets.Select(attrs={'class': 'form-control'}))
    print("shop_type_quere",shop_type_quere)

    def __init__(self, *args, **kwargs):
        super(Class_Text, self).__init__(*args, **kwargs)
        self.fields['shop_type_quere'].choices = ((x.id, x.name) for x in models.BlogCtg.objects.all())

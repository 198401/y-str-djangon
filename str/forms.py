#coding=utf-8
from django import forms

class SearchForm(forms.Form):

    str1 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS388')
    str2 = forms.IntegerField(required=False, min_value=0, max_value=99, label=ur'DYS19/394')
    str3 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS389I')
    str4 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS389II')
    str5 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS390')
    str6 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS391')
    str7 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS392')
    str8 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS393')
    str9 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS425')
    str10 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS426')
    str11 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS434')
    str12 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS435')
    str13 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS436')
    str14 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS437')
    str15 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS438')
    str16 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS439')
    str17 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS385a')
    str18 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS385b')
    str19 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYSA7.2')
    str20 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'Y GATE H4')
    str21 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS448')
    str22 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS456')
    str23 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS458')
    str24 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'DYS635')
    str37 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'YCAIIa')
    str38 = forms.IntegerField(required=False, min_value=0, max_value=99, label=u'YCAIIb')
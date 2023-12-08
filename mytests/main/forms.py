from django import forms
from django.contrib.auth.models import User
from .models import Result, Tests
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ResultForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget = forms.HiddenInput)
    test = forms.ModelChoiceField(queryset=Tests.objects.all(), widget = forms.HiddenInput, empty_label=None)
    date = forms.DateTimeField
    tr = forms.IntegerField
    fs = forms.IntegerField
    comment = forms.Textarea

#   attrs = {'disabled': 'disabled'}
    class Meta:
        model = Result
        fields = ['user','test','date','tr', 'fs','comment']
        labels = {
            'user': 'Пользователь',
            'test': 'Тест',
#            'date': 'Дата теста',
            'tr': 'Коль-во правильных отв.',
            'fs': 'Коль-во неправильных отв.',
            'comment': 'Комментарий',
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'cols': 20, 'rows': 3
            }),
            'date': forms.DateTimeInput(attrs={
                'readonly': 'readonly',
                'size': 15
            }),
            'tr': forms.TextInput(attrs={
                'readonly': 'readonly',
                'size': 5
            }),
            'fs': forms.TextInput(attrs={
                'readonly': 'readonly',
                'size': 5
            })
        }

    def clean_comment(self):
        data = self.cleaned_data['comment']

        if len(data)<3:
            raise ValidationError(_('Invalid date - len(comment)<3'))

        return data

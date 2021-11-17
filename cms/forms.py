from django import forms
from django.forms import ModelForm
from cms.models import UserHealth
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date, datetime


class UserHealthForm(ModelForm):
    """ユーザーBMIのフォーム"""
    class Meta:
        model = UserHealth
        fields = ('date', 'Height', 'Weight')
        widgets = {'date': AdminDateWidget(), }
        initial = {'date': date.today()}
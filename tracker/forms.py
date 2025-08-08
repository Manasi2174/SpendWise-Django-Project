# tracker/forms.py
from django import forms
from .models import Income, Expense, Category

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['category', 'amount', 'date', 'description']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'date', 'description']

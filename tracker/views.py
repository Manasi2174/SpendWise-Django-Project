from django.shortcuts import render,redirect
from .models import Income,Expense,Category
from .forms import IncomeForm,ExpenseForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.contrib import messages



# Create your views here.
@login_required
def dashboard(request):
    print("Dashboard view called")
    incomes = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    total_income = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    # Prepare data for Chart
    expense_data = expenses.values('category__name').annotate(total=Sum('amount'))
    labels = [e['category__name'] for e in expense_data]
    data = [float(e['total']) for e in expense_data]

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'incomes': incomes,
        'expenses': expenses,
        'chart_labels': labels,
        'chart_data': data,
    }
    return render(request, 'tracker/dashboard.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Income'})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Add Expense'})

@login_required
def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    form = IncomeForm(request.POST or None, instance=income)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Edit Income'})

@login_required
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    income.delete()
    return redirect('dashboard')

@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'tracker/form.html', {'form': form, 'title': 'Edit Expense'})

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect('dashboard')
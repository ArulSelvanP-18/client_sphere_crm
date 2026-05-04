from django.shortcuts import render, redirect
from .models import Account, Transaction

# LIST + SEARCH
def account_list(request):
    query = request.GET.get('q')

    if query:
        accounts = Account.objects.filter(name__icontains=query)
    else:
        accounts = Account.objects.all()

    return render(request, 'accounts.html', {'accounts': accounts})


# ADD ACCOUNT
def add_account(request):
    if request.method == "POST":
        name = request.POST.get("name")
        balance = request.POST.get("balance")

        acc = Account.objects.create(name=name, balance=balance)

        return redirect('accounts')
    
    return render(request, 'add_account.html')


# EDIT ACCOUNT
def edit_account(request, id):
    acc = Account.objects.get(id=id)

    if request.method == "POST":
        acc.name = request.POST.get("name")
        acc.balance = request.POST.get("balance")
        acc.save()
        return redirect('accounts')

    return render(request, 'edit_account.html', {'acc': acc})


# DEACTIVATE
def deactivate_account(request, id):
    acc = Account.objects.get(id=id)
    acc.status = "Inactive"
    acc.save()
    return redirect('accounts')


# TRANSACTION HISTORY
def transaction_history(request, id):
    acc = Account.objects.get(id=id)
    transactions = Transaction.objects.filter(account=acc)

    return render(request, 'transactions.html', {
        'acc': acc,
        'transactions': transactions
    })
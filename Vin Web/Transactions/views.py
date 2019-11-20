from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Transaction

def index(request):
    return render(request, 'Transactions/index.html')

def detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk = transaction_id)
    context = { 'transaction': transaction }
    return render(request, 'Transactions/detail.html', context)

def add_manual(request):
    if request.method == 'POST':
        t = Transaction(request.POST['Amount'],
                        '-',
                        request.POST['Currency'],
                        request.POST['Date'],
                        request.POST['Account'],
                        request.POST['Comment'])
    return render(request, 'Transactions/manual_add.html')
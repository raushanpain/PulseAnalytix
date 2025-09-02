from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def payment(request):
    return render(request, 'payments/payment.html')

@login_required
def payment_history(request):
    return render(request, 'payments/history.html')
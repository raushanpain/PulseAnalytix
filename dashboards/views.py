from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard1(request):
    return render(request, 'dashboards/dashboard1.html')

@login_required
def dashboard2(request):
    return render(request, 'dashboards/dashboard2.html')

@login_required
def dashboard3(request):
    return render(request, 'dashboards/dashboard3.html')

@login_required
def dashboard4(request):
    return render(request, 'dashboards/dashboard4.html')
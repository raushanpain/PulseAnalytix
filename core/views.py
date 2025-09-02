from django.shortcuts import render

def home(request):
    """Render the home page with navigation to different dashboards"""
    return render(request, 'core/home.html')

def about(request):
    """Render the about page"""
    return render(request, 'core/about.html')
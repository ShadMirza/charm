from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def charm(request):
    return render(request, 'charm.html')
def contact(request):
    return render(request, 'contact.html')
def team(request):
    return render(request, 'team.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
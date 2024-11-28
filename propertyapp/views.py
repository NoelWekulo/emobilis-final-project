from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def properties(request):
    return render(request, 'properties.html')
def services(request):
    return render(request, 'services.html')

def propertySingle(request):
    return render(request, 'propertySingle.html')
def blog(request):
    return render(request, 'blog.html')
def agent(request):
    return render(request, 'agent.html')

def listing(request):
    return render(request, 'listing.html')

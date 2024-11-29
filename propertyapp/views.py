from django.shortcuts import render,redirect
from .models import (
    Testimonial,Property,Agent,Blog,BlogCategory,
    AgentApplication,ContactInfo, Message,Service,Team,PropertyImage
)

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse

from django.contrib import messages


# Create your views here.
def common_data():
    categories = BlogCategory.objects.all()
    testimonials = Testimonial.objects.all()
    for testimonial in testimonials:
        testimonial.stars = range(testimonial.rating)  # Add a stars property
    
    return {
        'testimonials': testimonials,
        'categories': categories,
    }
def index(request):
    featured_properties = Property.objects.filter(featured=True)[:10]
    agents = Agent.objects.all()[:5]
    recent_blogs = Blog.objects.all().order_by("-created_at")[:3]

    return render(request, 'index.html', {
        'featured_properties': featured_properties,
        'agents': agents,
        'blogs': recent_blogs,
        **common_data()
    })

def property_single(request, pk):
    property = get_object_or_404(Property, pk=pk)
    propertyimages = PropertyImage.objects.filter(property= property)
    return render(request, 'property-single.html', {'property': property, 'propertyimages':propertyimages,  **common_data()})
def apply_agent(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        AgentApplication.objects.create(name=name, email=email, phone=phone, message=message)
        return HttpResponse("Application submitted successfully!")
    return render(request, 'apply_agent.html',)

def contact(request):
    contact_info = ContactInfo.objects.first()  # Assuming one contact info object
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message_text = request.POST['message']
        Message.objects.create(name=name, email=email, subject=subject, message=message_text)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('/contact/')
    return render(request, 'contact.html', {'contact_info': contact_info,  **common_data()})




def blog_list(request, slug=None):
    if slug:
        category = get_object_or_404(BlogCategory, slug=slug)
        blogs = Blog.objects.filter(category=category)
    else:
        blogs = Blog.objects.all()

    # Paginate blogs: 5 per page
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {'page_obj': page_obj, 'category': slug,   **common_data()})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog,  **common_data()})

def services(request):
    services = Service.objects.all()

    return render(request, 'services.html', {'services': services,  **common_data()})

def about(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {'teams': teams,  **common_data()})
def buy(request):
    return render(request, 'buy.html', {**common_data()})
def sale(request):
    return render(request, 'sale.html')

def propertysingle(request):
    return render(request, 'property-single.html')
def blog(request):
    return render(request, 'blog.html')
def agent(request):
    agents = Agent.objects.all()[:5]
    return render(request, 'agent.html', {'agents': agents,  **common_data()})


def listing(request):
    return render(request, 'listing.html')
def properties(request):
    properties = Property.objects.all()
    featured_properties = Property.objects.filter(featured=True)[:10]
    return render(request, 'properties.html', {
        'featured_properties': featured_properties,
        'properties': properties, 
        **common_data()
    })

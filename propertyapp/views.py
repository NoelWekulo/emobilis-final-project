from django.shortcuts import render,redirect
from .models import (
    Testimonial,Property,Agent,Blog,BlogCategory,
    AgentApplication,ContactInfo, Message,Service,Team,PropertyImage,Profile
)
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ProfileUpdateForm,RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login


# Create your views here.
def common_data(request):
    categories = BlogCategory.objects.all()
    testimonials = Testimonial.objects.all()
    profile=""
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
       
    for testimonial in testimonials:
        testimonial.stars = range(testimonial.rating)  # Add a stars property
    
    return {
        'testimonials': testimonials,
        'categories': categories,
        'profile': profile,  # Add the profile to the context if user is authenticated
    }
def index(request):
    featured_properties = Property.objects.filter(featured=True)
    agents = Agent.objects.all()
    recent_blogs = Blog.objects.all().order_by("-created_at")

    return render(request, 'index.html', {
        'featured_properties': featured_properties,
        'agents': agents,
        'blogs': recent_blogs,
        **common_data(request)
    })

def property_single(request, pk):
    property = get_object_or_404(Property, pk=pk)
    propertyimages = PropertyImage.objects.filter(property= property)
    return render(request, 'property-single.html', {'property': property, 'propertyimages':propertyimages,  **common_data(request)})
def apply_agent(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        AgentApplication.objects.create(name=name, email=email, phone=phone, message=message)
        return HttpResponse("Application submitted successfully!")
    return render(request, 'apply_agent.html', {**common_data(request)})

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
    return render(request, 'contact.html', {'contact_info': contact_info,  **common_data(request)})




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

    return render(request, 'blog.html', {'page_obj': page_obj, 'category': slug,   **common_data(request)})


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'blog': blog,  **common_data(request)})

def services(request):
    services = Service.objects.all()

    return render(request, 'services.html', {'services': services,  **common_data(request)})

def about(request):
    teams = Team.objects.all()
    return render(request, 'about.html', {'teams': teams,  **common_data(request)})
def buy(request):
    return render(request, 'buy.html', {**common_data(request)})
def sale(request):
    return render(request, 'sale.html', {**common_data(request)})

def propertysingle(request):
    return render(request, 'property-single.html',{**common_data(request)})
def blog(request):
    blogs = Blog.objects.all()
     # Paginate blogs: 5 per page
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {'page_obj': page_obj, 'category': 'all',   **common_data(request)})

def agent(request):
    agents = Agent.objects.all()
    return render(request, 'agent.html', {'agents': agents,  **common_data(request)})


def listing(request):
    return render(request, 'listing.html', {**common_data(request)})
def properties(request):
    properties = Property.objects.all()
    featured_properties = Property.objects.filter(featured=True)
    return render(request, 'properties.html', {
        'featured_properties': featured_properties,
        'properties': properties, 
        **common_data(request)
    })
# views.py


def buy_properties(request):
    """Display properties available for buying."""
    properties = Property.objects.filter(property_type='buy')
    return render(request, 'buy.html', {'properties': properties, **common_data(request)})


@login_required
def sell_property(request):
    """Handle property creation for selling."""
    if request.method == 'POST':
        # Get form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        address = request.POST.get('address')
        location = request.POST.get('location')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        image = request.FILES.get('image')
        agent_name = request.POST.get('agent_name')
        agent_image = request.FILES.get('agent_image')
        agent_description = request.POST.get('agent_description')

        # Create and save property
        Property.objects.create(
            title=title,
            description=description,
            price=price,
            address=address,
            location=location,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            image=image,
            property_type='sell',
            agent_name=agent_name,
            agent_image=agent_image,
            agent_description=agent_description,
        )
        return redirect('propertyapp:sell_success')  # Redirect to a success page or refresh
    return render(request, 'sell.html')



def sell_success(request):
    """Display a success message after a property is submitted."""
    return render(request, 'sell_success.html')



def listings(request, category=None):
    #Display listings filtered by category.
    if category:
        properties = Property.objects.filter(property_type='listings', category=category)
    else:
        properties = Property.objects.filter(property_type='listings')
    return render(request, 'listings.html', {'properties': properties, 'category': category, **common_data(request) })

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('/')
    return render(request, 'accounts/register.html', {'form': form,**common_data(request) })


# def register(request):
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
#         gender = request.POST.get('gender')

#         # Validate password
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match')
#             return render(request, 'registration.html')

#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return render(request, 'register.html')

#         # Create user
#         try:
#             user = User.objects.create_user(
#                 username=username, 
#                 email=email, 
#                 password=password
#             )
#             user.first_name = full_name
#             user.save()
            
#             # Add success message
#             messages.success(request, 'You have successfully registered! Please login.')
#             return redirect('login')
#         except Exception as e:
#             messages.error(request, f'Registration failed: {str(e)}')
#             return render(request, 'register.html')

#     return render(request, 'register.html')


@login_required
def profile(request):
    """Allow users to update their profile picture."""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('propertyapp:profile')  # Redirect to the profile page after saving
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {'form': form,**common_data(request) })
def logout_user(request):
    logout(request)
    return redirect('/')




# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('dashboard')  # Redirect to dashboard after login
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'login.html')
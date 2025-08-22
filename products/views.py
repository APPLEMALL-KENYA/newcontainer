from django.shortcuts import render
from .models import Product, Slider, Testimonial, CompanyInfo

def home(request):
    # Fetch active sliders
    sliders = Slider.objects.filter(is_active=True).order_by("id")

    # Fetch products with optimized related image loading
    products = Product.objects.prefetch_related("images").all()

    # Fetch latest 6 testimonials
    testimonials = Testimonial.objects.order_by("-created_at")[:6]

    # Get the first (and only) company info instance, if it exists
    company_info = CompanyInfo.objects.first()

    # Context for the homepage
    context = {
        "title": "Welcome to Containers App",
        "description": "Your one-stop solution for quality containers!",
        "sliders": sliders,
        "products": products,
        "testimonials": testimonials,
        "company_info": company_info,
    }

    return render(request, "products/home.html", context)

from django.shortcuts import render
from .models import Product, Slider, Testimonial

def home(request):
    # Fetch active sliders
    sliders = Slider.objects.filter(is_active=True).order_by("id")

    # Fetch products with optimized related image loading
    products = Product.objects.prefetch_related("images").all()

    # Fetch latest testimonials (limit 6)
    testimonials = Testimonial.objects.order_by("-created_at")[:6]

    # Context for the homepage template
    context = {
        "title": "Welcome to Containers App",
        "description": "Your one-stop solution for quality containers!",
        "sliders": sliders,
        "products": products,
        "testimonials": testimonials,
    }

    return render(request, "products/home.html", context)

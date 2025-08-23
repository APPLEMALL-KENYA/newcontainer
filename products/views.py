from django.shortcuts import render, get_object_or_404
from .models import Product, ProductGallery, Slider, Testimonial, CompanyInfo

# -------------------------
# HOME PAGE VIEW
# -------------------------
def home(request):
    # Fetch active sliders
    sliders = Slider.objects.filter(is_active=True).order_by("id")

    # Fetch products and prefetch related gallery images
    products = Product.objects.prefetch_related("gallery").all()

    # Provide default images where necessary
    for product in products:
        # Default main image
        if hasattr(product, "image") and product.image:
            product.image_url = product.image.url
        else:
            product.image_url = "/static/images/default-product.jpg"

        # Prepare gallery thumbnails (limit 3)
        product.gallery_images = []
        for thumb in product.gallery.all():
            if thumb.image:
                product.gallery_images.append(thumb.image.url)
            else:
                product.gallery_images.append("/static/images/default-product.jpg")
        product.gallery_images = product.gallery_images[:3]

    # Fetch latest 6 testimonials
    testimonials = Testimonial.objects.order_by("-created_at")[:6]

    # Fetch company info if available
    company_info = CompanyInfo.objects.all())

    context = {
        "title": "Welcome to Containers App",
        "description": "Your one-stop solution for quality containers!",
        "sliders": sliders,
        "products": products,
        "testimonials": testimonials,
        "company_info": company_info,
    }
    return render(request, "products/home.html", context)


# -------------------------
# PRODUCT DETAIL VIEW
# -------------------------
def product_detail(request, pk):
    # Fetch a single product with its gallery images
    product = get_object_or_404(Product.objects.prefetch_related("gallery"), pk=pk)

    # Related products (optional)
    related_products = Product.objects.exclude(pk=pk)[:4]

    context = {
        "product": product,
        "related_products": related_products,
    }
    return render(request, "products/product_detail.html", context)


# -------------------------
# PRODUCT LIST VIEW
# -------------------------
def products_list(request):
    # Fetch all products with gallery images
    products = Product.objects.prefetch_related("gallery").all()

    # Assign default images for missing product images
    for product in products:
        if hasattr(product, "image") and product.image:
            product.image_url = product.image.url
        else:
            product.image_url = "/static/images/default-product.jpg"

    return render(request, "products/products_list.html", {"products": products})

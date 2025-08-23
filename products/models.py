from django.db import models


# -----------------------
# Slider Model
# -----------------------
class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle1 = models.CharField(max_length=300, blank=True, null=True)
    subtitle2 = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='slider_images/')
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# -----------------------
# Product Model
# -----------------------
class Product(models.Model):
    STOCK_CHOICES = [
        ("in_stock", "In Stock"),
        ("out_of_stock", "Out of Stock"),
    ]

    name = models.CharField(max_length=255)
    description_1 = models.TextField("Description 1", blank=True, null=True)
    description_2 = models.TextField("Description 2", blank=True, null=True)
    description_3 = models.TextField("Description 3", blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_status = models.CharField(max_length=20, choices=STOCK_CHOICES, default="in_stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    
# -----------------------
# Product Image Model
# -----------------------
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"


# -----------------------
# Product Gallery Model
# -----------------------
class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"


# -----------------------
# Testimonial Model
# -----------------------
class Testimonial(models.Model):
    name = models.CharField(max_length=100, default="Anonymous")
    designation = models.CharField(max_length=100, blank=True, null=True)
    feedback = models.TextField(default="No feedback provided.")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name


# -----------------------
# Company Info Model
# -----------------------
class CompanyInfo(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    email = models.EmailField(default="containerspaces@gmail.com")
    phone = models.CharField(max_length=20, default="0000000000")
    address = models.TextField(default="Not provided")
    location_url = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



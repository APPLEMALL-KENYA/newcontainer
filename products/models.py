from django.db import models

# Create your models here.
from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle1 = models.CharField(max_length=300, blank=True, null=True)
    subtitle2 = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="sliders/")
    image = models.ImageField(upload_to='slider_images/')
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


from django.db import models

from django.db import models

class Product(models.Model):
    STOCK_CHOICES = [
        ("in_stock", "In Stock"),
        ("out_of_stock", "Out of Stock"),
    ]

    name = models.CharField(max_length=255)
    description_1 = models.TextField("Description 1", blank=True, null=True)
    description_2 = models.TextField("Description 2", blank=True, null=True)
    description_3 = models.TextField("Description 3", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_status = models.CharField(max_length=20, choices=STOCK_CHOICES, default="in_stock")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"

# products/models.py
from django.db import models

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()  # <- This is the message entered in admin
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


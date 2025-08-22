from django.db import models

# Slider Model
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


# Product Model
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

    def __str__(self):
        return self.name


# ProductImage Model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"


# Testimonial Model
class Testimonial(models.Model):
    customer_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

def get_image(self):
    image = self.images.first()
    if image:
        return image.image.url
    return '/media/product_images/default.jpg'  # No space!

class CompanyInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title



from django.contrib import admin
from .models import Slider, Product, ProductImage

# ---------------- Slider Admin ---------------- #
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle1', 'subtitle2', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle1', 'subtitle2')


# ---------------- Product Images Inline ---------------- #
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Show 3 empty fields by default
    fields = ("image",)
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width:80px;height:80px;object-fit:cover;border-radius:6px;" />'
        return "No Image"
    preview.allow_tags = True


# ---------------- Product Admin ---------------- #
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock_status", "created_at")
    list_filter = ("stock_status", "created_at")
    search_fields = ("name", "description_1", "description_2", "description_3")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    inlines = [ProductImageInline]
    
    fieldsets = (
        ("Product Details", {
            "fields": (
                "name",
                "price",
                "stock_status",
                "description_1",
                "description_2",
                "description_3"
            )
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'rating', 'created_at')  # ✅ Use existing fields
    search_fields = ('customer_name', 'message')
    list_filter = ('rating', 'created_at')

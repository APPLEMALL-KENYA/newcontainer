from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Slider,
    Product,
    ProductImage,
    ProductGallery,
    Testimonial,
    CompanyInfo,
)

# ---------------- Slider Admin ---------------- #
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle1', 'subtitle2', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle1', 'subtitle2')


# ---------------- Product Images Inline ---------------- #
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # Show 3 empty image fields by default
    fields = ("image", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:80px; height:80px; object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "No Image"

    preview.short_description = "Preview"


# ---------------- Product Gallery Inline ---------------- #
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


# ---------------- Product Admin ---------------- #
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock_status", "created_at")
    list_filter = ("stock_status", "created_at")
    search_fields = ("name", "description_1", "description_2", "description_3")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    inlines = [ProductImageInline, ProductGalleryInline]

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


# ---------------- Product Gallery Admin ---------------- #
@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ("product", "id")


# ---------------- Testimonial Admin ---------------- #
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'rating', 'created_at')
    list_filter = ('created_at', 'rating')
    search_fields = ('name', 'designation', 'feedback')


# ---------------- Company Info Admin ---------------- #
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'updated_at')
    readonly_fields = ('updated_at',)

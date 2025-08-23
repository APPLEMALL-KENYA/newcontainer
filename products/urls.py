from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    # urls.py
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    
    # urls.py
    
# urls.py
    



]

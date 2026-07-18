from django.urls import path
from Catalog import views

urlpatterns = [
    path("", views.index, name="index"),
    path('About/', views.about,name='about'),
    path('Products/', views.products,name='products'),
    path('Brand/',views.brand,name='brand'),
    path('Contact/', views.contact,name='contact'), 
    path('Login/', views.Login,name = 'Login'),
    path('SignUp/', views.SignUp,name = 'SignUp'),
]

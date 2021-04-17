from django.urls import path

from . import views

app_name = 'supersub'

urlpatterns = [
    path('', views.index, name='index'),
    path('product_detail/<int:id_product>', views.product_detail, name='product_detail'),
    path('registered_products/', views.registered_products, name='registered_products'),
    path('results/', views.results, name='results'),
    path('register_product/<int:id_product>/<int:id_user>', views.register_product, name='register_product'),
]

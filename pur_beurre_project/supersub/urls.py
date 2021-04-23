from django.urls import path

from . import views
from .views import IndexView, ProductDetailView, FavoritesView

app_name = 'supersub'

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
   
    path('product_detail/<int:id_product>', ProductDetailView.as_view(), name='product_detail'),
    # path('product_detail/<int:id_product>', views.product_detail, name='product_detail'),

    path('favorites/', FavoritesView.as_view(), name='favorites'),
    # path('registered_products/', views.registered_products, name='registered_products'),

    path('results/', views.results, name='results'),
    # path('results_test/', views.results_test, name='results_test'),
    path('register_product/<int:id_product>/<int:id_user>', views.register_product, name='register_product'),
]

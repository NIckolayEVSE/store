from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product'),
    # path('category/<int:category_id>', views.products, name='category'),
    # path('page/<int:page_number>', views.products, name='paginator'),
    path('category/<int:category_id>/', views.ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_pk>', views.basket_remove, name='basket_remove'),
]

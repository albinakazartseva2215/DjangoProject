from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactsView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/contacts/", ContactsView.as_view(), name="contacts"),
    path("catalog/product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/product_create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete")
]

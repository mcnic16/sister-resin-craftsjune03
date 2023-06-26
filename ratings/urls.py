from django.urls import path
from ratings.views import rate_product

urlpatterns = [
    path('rate-product/', rate_product, name='rate_product'),
]
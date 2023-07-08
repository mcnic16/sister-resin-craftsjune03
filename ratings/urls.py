from django.urls import path
from ratings import views


urlpatterns = [
    path("rate/<int:product_id>/", views.rate_product, name="rate_product"),
    path("ratings/", views.show_ratings, name="show_ratings"),
    path('edit_rating/<int:rating_id>/', views.edit_rating, name='edit_rating'),
]

from django.urls import path
from queries import views


urlpatterns = [
    path('queries/', views.aboutus, name='queries'),
]
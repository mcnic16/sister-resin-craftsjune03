from django.urls import path
from queries import views
from .views import SubmitQueryView


urlpatterns = [
    path('', views.aboutus, name='queries'),
    path('queries/submit/', views.SubmitQueryView.as_view(), name='submit_query'),
]
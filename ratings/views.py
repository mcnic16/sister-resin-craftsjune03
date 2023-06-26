from django.shortcuts import render, redirect
from .models import Rating

def rate_product(request):
    if request.method == 'POST':
        stars = request.POST.get('stars')
        rating = Rating.objects.create(user=request.user, stars=stars)
        
        return redirect('product_detail')  # Redirect to the appropriate page after rating.
    return render(request, 'ratings/rate_product.html')  # Display the rating form.
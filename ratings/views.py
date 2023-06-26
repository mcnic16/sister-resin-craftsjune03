from django.shortcuts import render, redirect
from .models import Rating

def rate_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        user = request.user
        stars = int(request.POST.get('stars'))
        comment = request.POST.get('comment')

        Rating.objects.create(product=product, user=user, stars=stars, comment=comment)

        return redirect('ratings:show_ratings')

    return render(request, 'ratings/rate_product.html')

def show_ratings(request):
    ratings = Rating.objects.all()
    return render(request, 'ratings/show_ratings.html', {'ratings': ratings})

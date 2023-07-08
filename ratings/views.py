from django.shortcuts import render, redirect
from .models import Rating
from products.models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def rate_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        stars = int(request.POST.get("stars"))
        comment = request.POST.get("comment")
        Rating.objects.create(product=product, stars=stars, comment=comment)

    context = {"product_id": product.id}
    return render(request, "ratings/rate_product.html", context)


def show_ratings(request):
    ratings = Rating.objects.all()
    for rating in ratings:
        rating.stars = [1] * rating.stars
    context = {"ratings": ratings}
    return render(request, "ratings/show_ratings.html", context)


@login_required
def edit_rating(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.method == "POST":
        rating.stars = int(request.POST.get("stars"))
        rating.comment = request.POST.get("comment")
        rating.save()
        return redirect('show_ratings')

    context = {"rating": rating}
    return render(request, "ratings/edit_rating.html", context)


@login_required
def delete_rating(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id)
    if request.method == "POST":
        rating.delete()
        return redirect('show_ratings')

    context = {"rating": rating}
    return render(request, "ratings/delete_rating.html", context)



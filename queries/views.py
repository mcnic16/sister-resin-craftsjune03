from django.shortcuts import render


def aboutus(request):
    """ A view to return the queries page """

    return render(request, 'queries/queries.html')

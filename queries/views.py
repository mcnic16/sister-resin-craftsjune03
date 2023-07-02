from django.shortcuts import render, redirect
from .models import Query
from .forms import QueryForm


def aboutus(request):
    """ A view to return the queries page """

    return render(request, 'queries/queries.html')


def submit_query(request):
    if request.method == 'POST':
        query_form = QueryForm(request.POST)
        if query_form.is_valid():
            query_form.save()
            return redirect('submit_query')
    else:
        query_form = QueryForm()

    context = {
        'query_form':query_form,
            }
    return render(request, 'queries/queries.html', context)

    

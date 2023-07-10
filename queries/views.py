from django.shortcuts import render, redirect
from .models import Query
from django.views import generic, View
from .forms import QueryForm


class SubmitQueryView(View):
    """ A view to submit a query """
    def get(self, request):
        query_form = QueryForm()
        return render(
            request,
            "queries/submit_query.html",
            {"query_form": query_form},
        )

    def post(self, request):
        query_form = QueryForm(request.POST)
        if query_form.is_valid():
            query_form.save()
            return redirect("submit_query")
        return render(request, "queries/submit_query.html", {"query_form": query_form})


def aboutus(request):
    """A view to return the queries page"""
    return render(request, "queries/queries.html")

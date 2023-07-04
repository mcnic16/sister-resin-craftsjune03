from django.contrib import admin
from .models import Rating


class RatingsAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "stars",
        "comment",
        "date",
    )


admin.site.register(Rating, RatingsAdmin)

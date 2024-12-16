from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "", include("tax_calculator.urls")
    ),  # Inclure uniquement les URLs des applications
]

from django.urls import path

from .views import (
    convert,
    delete_conversion,
    get_units_by_dimension,
    index,
    save_conversion,
)

urlpatterns = [
    path("", index, name="index"),
    path("convert/", convert, name="convert"),
    path("get-units/", get_units_by_dimension, name="get_units_by_dimension"),
    path("save-conversion/", save_conversion, name="save_conversion"),
    path("delete-conversion/<int:pk>/", delete_conversion, name="delete_conversion"),
]

from django.urls import path

from .views import (
    index,
    convert,
    get_units_by_dimension,
    save_conversion,
)

urlpatterns = [
    path("", index, name="index"),
    path("convert/", convert, name="convert"),
    path("get-units/", get_units_by_dimension, name="get_units_by_dimension"),
    path("save-conversion/", save_conversion, name="save_conversion"),
]

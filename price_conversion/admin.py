from django.contrib import admin

from .models import Conversion, ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ("currency", "rate", "date")


@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = (
        "from_price",
        "from_currency",
        "from_unit",
        "to_price",
        "to_currency",
        "to_unit",
    )

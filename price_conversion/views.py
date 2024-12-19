from django.shortcuts import get_object_or_404, render
from .models import Conversion, ExchangeRate
from .enums.currency import Currency
from .enums.unit import Unit


def index(request):
    conversions = Conversion.objects.all()
    currencies = list(Currency)
    units = list(Unit)
    context = {
        "conversions": conversions,
        "currencies": currencies,
        "units": units,
    }
    return render(request, "price_conversion/index.html", context)


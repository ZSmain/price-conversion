from decimal import Decimal

import requests
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .enums.currency import Currency
from .enums.unit import Unit
from .models import Conversion, ExchangeRate


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


def convert(request):
    if request.method == "POST":
        from_currency_code = request.POST.get("from_currency")
        to_currency_code = request.POST.get("to_currency")
        from_price = Decimal(request.POST.get("from_price"))
        from_unit_code = request.POST.get("from_unit")
        to_unit_code = request.POST.get("to_unit")

        # Convert currency codes to Currency enums
        from_currency = Currency[from_currency_code]
        to_currency = Currency[to_currency_code]

        # Check and retrieve exchange rates
        # Base currency is EUR
        exchange_rates = {}
        currencies = [from_currency, to_currency]
        for currency in currencies:
            if currency == Currency.EUR:
                exchange_rates[currency] = 1.0
                continue
            try:
                exchange_rate = ExchangeRate.objects.get(currency=currency)
                exchange_rates[currency] = float(exchange_rate.rate)
            except ExchangeRate.DoesNotExist:
                # Fetch exchange rate from API and save
                api_url = f"https://v6.exchangerate-api.com/v6/{settings.EXCHANGE_RATE_API_KEY}/pair/EUR/{currency.value}"
                response = requests.get(api_url)
                data = response.json()
                if data.get("result", "") == "success":
                    rate = data["conversion_rate"]
                    ExchangeRate.objects.create(
                        currency=currency,
                        rate=Decimal(rate),
                        date=timezone.datetime.strptime(
                            data["time_last_update_utc"], "%a, %d %b %Y %H:%M:%S %z"
                        ).date(),
                    )
                    exchange_rates[currency] = rate
                else:
                    return JsonResponse({"error": "Failed to fetch exchange rates"})

        # Convert from_price to EUR
        from_price_in_eur = from_price / Decimal(exchange_rates[from_currency])
        # Convert EUR to to_currency
        converted_price = from_price_in_eur * Decimal(exchange_rates[to_currency])

        # Perform unit conversion
        from_unit = Unit[from_unit_code]
        to_unit = Unit[to_unit_code]
        if from_unit.dimension == to_unit.dimension:
            # Convert to base unit
            from_quantity_in_base = converted_price * Decimal(from_unit.units_to_base)
            # Convert to target unit
            final_price = from_quantity_in_base / Decimal(to_unit.units_to_base)
        else:
            return JsonResponse({"error": "Units are not compatible"})

        context = {
            "from_price": from_price,
            "from_currency_symbol": from_currency.symbol,
            "from_unit": from_unit.symbol,
            "converted_price": round(final_price, 4),
            "to_currency_symbol": to_currency.symbol,
            "to_unit": to_unit.symbol,
            "conversion_rate": exchange_rates[to_currency]
            / exchange_rates[from_currency],
        }

        return render(request, "price_conversion/conversion_result.html", context)

    return HttpResponse("Invalid request", status=400)


def get_units_by_dimension(request):
    unit_value = request.GET.get("from_unit")
    try:
        selected_unit = Unit[unit_value]
        if selected_unit and selected_unit.dimension:
            compatible_units = [
                unit
                for unit in Unit
                if unit.dimension == selected_unit.dimension and unit.can_be_priced
            ]
            # Return only the options HTML
            return render(
                request,
                "price_conversion/unit_options.html",
                {"units": compatible_units},
            )
    except (KeyError, AttributeError):
        pass
    return HttpResponse("")


def save_conversion(request):
    if request.method == "POST":
        try:
            from_price = Decimal(request.POST["from_price"])
            from_currency = Currency[request.POST["from_currency"]]
            from_unit = Unit[request.POST["from_unit"]]
            # Calculate the to_price from the result
            exchange_rates = {}
            currencies = [from_currency, Currency[request.POST["to_currency"]]]

            for currency in currencies:
                if currency == Currency.EUR:
                    exchange_rates[currency] = 1.0
                    continue
                try:
                    exchange_rate = ExchangeRate.objects.get(currency=currency)
                    exchange_rates[currency] = float(exchange_rate.rate)
                except ExchangeRate.DoesNotExist:
                    return JsonResponse({"error": "Exchange rate not found"})

            # Convert price
            to_currency = Currency[request.POST["to_currency"]]
            to_unit = Unit[request.POST["to_unit"]]

            # Convert to EUR first
            from_price_in_eur = from_price / Decimal(exchange_rates[from_currency])
            # Convert EUR to target currency
            converted_price = from_price_in_eur * Decimal(exchange_rates[to_currency])

            # Convert units
            if from_unit.dimension == to_unit.dimension:
                from_quantity_in_base = converted_price * Decimal(
                    from_unit.units_to_base
                )
                final_price = from_quantity_in_base / Decimal(to_unit.units_to_base)
            else:
                return JsonResponse({"error": "Units are not compatible"})

            conversion = Conversion.objects.create(
                from_price=from_price,
                from_currency=from_currency,
                from_unit=from_unit,
                to_price=round(final_price, 4),
                to_currency=to_currency,
                to_unit=to_unit,
            )

            return render(
                request,
                "price_conversion/conversion_row.html",
                {"conversion": conversion},
            )
        except (KeyError, ValueError) as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request"})


def delete_conversion(request, pk):
    conversion = get_object_or_404(Conversion, pk=pk)
    conversion.delete()
    return HttpResponse("")


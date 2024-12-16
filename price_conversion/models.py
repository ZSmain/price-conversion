from decimal import Decimal as Dec

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.flexup_enum_field import FlexUpEnumField
from price_conversion.enums.currency import Currency
from price_conversion.enums.unit import Unit


# EUR is the base currency
class ExchangeRate(models.Model):
    currency: Currency = FlexUpEnumField(
        flexup_enum=Currency, verbose_name=_("Currency"), choices=Currency.choices
    )  # eg. 'USD'
    rate: Dec = models.DecimalField(
        verbose_name=_("Rate"), max_digits=15, decimal_places=6
    )  # eg. 0.95  -> 1 USD = 0.95 EUR
    date = models.DateField(verbose_name=_("Date"), auto_now_add=True)


class Conversion(models.Model):
    from_price: Dec = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name=_("Price")
    )
    from_currency: Currency = FlexUpEnumField(
        flexup_enum=Currency, verbose_name=_("Currency"), choices=Currency.choices
    )
    from_unit: Unit = FlexUpEnumField(
        flexup_enum=Unit,
        verbose_name=_("System unit"),
        choices=Unit.choices,
        null=True,
        blank=True,
    )
    to_price: Dec = models.DecimalField(
        max_digits=15, decimal_places=4, verbose_name=_("Price")
    )
    to_currency: Currency = FlexUpEnumField(
        flexup_enum=Currency, verbose_name=_("Currency"), choices=Currency.choices
    )
    to_unit: Unit = FlexUpEnumField(
        flexup_enum=Unit,
        verbose_name=_("System unit"),
        choices=Unit.choices,
        null=True,
        blank=True,
    )

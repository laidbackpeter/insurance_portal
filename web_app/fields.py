from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from datetime import date

# Validator for charfield to be all lowercase


def validate_lower(value):
    """Validate that all inputs are in lower case for uniformity"""
    if not value.islower():
        raise ValidationError(
            _('%(value)s is not in lower case'),
            params={'value': value},
        )


def validate_not_future(value):
    """Validate that year of manufature is not in the future"""
    this_year = date.today().year
    if value > this_year:
        raise ValidationError(
            _('Year of manufacture cannot be in the future'),
        )


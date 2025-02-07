"""
Country model module.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import ModelBase


class ModelCountry(ModelBase):
    """
    Country model for the application.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("Country Name"),
        help_text=_("The official name of the country."),
    )
    alpha2_code = models.CharField(
        max_length=2,
        unique=True,
        verbose_name=_("Alpha-2 Code"),
        help_text=_(
            "The ISO 3166-1 alpha-2 code (e.g., 'US' for United States)."
        ),
    )
    alpha3_code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name=_("Alpha-3 Code"),
        help_text=_(
            "The ISO 3166-1 alpha-3 code (e.g., 'USA' for United States)."
        ),
    )
    numeric_code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name=_("Numeric Code"),
        help_text=_(
            "The ISO 3166-1 numeric code (e.g., '840' for United States)."
        ),
    )
    isd_code = models.CharField(
        max_length=5,
        unique=True,
        verbose_name=_("ISD Code"),
        help_text=_("The International Subscriber Dialing code."),
    )
    currency_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Currency Name"),
        help_text=_("The name of the currency used in the country."),
    )
    currency_alpha3 = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        verbose_name=_("Currency Alpha-3 Code"),
        help_text=_(
            "The ISO 4217 alpha-3 code for the currency (e.g., 'USD' for US Dollar)."
        ),
    )
    currency_numeric_code = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        verbose_name=_("Currency Numeric Code"),
        help_text=_(
            "The ISO 4217 numeric code for the currency (e.g., '840' for USD)."
        ),
    )
    currency_symbol = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_("Currency Symbol"),
        help_text=_(
            "The symbol used to represent the currency (e.g., '$', '€')."
        ),
    )

    class Meta:
        """Class Meta"""

        db_table = "country"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = ["name"]

    def __str__(self):
        """
        Returns a string representation of the country model object.

        :return: A string representing the name of the country.
        :rtype: str
        """
        # Return the name of the country.
        return str(self.name)

    @classmethod
    def get_country(cls, **kwargs):
        """
        Fetches and returns the country object that matches the given filter
        parameters.

        :param kwargs: A dictionary containing the filter parameters.
        :type kwargs: dict

        :return: The country object that matches the given filter parameters.
        :rtype: ModelCountry
        """

        # Get the country object that matches the given filter parameters
        country = cls.objects.get(**kwargs)

        # Return the country object
        return country

    @classmethod
    def get_countries(cls, **kwargs):
        """
        Fetches and returns a queryset of all the countries that match the
        given filter parameters.

        :param kwargs: A dictionary containing the filter parameters.
        :type kwargs: dict

        :return: A queryset of all the countries that match the given filter
        parameters.
        :rtype: django.db.models.query.QuerySet
        """

        # Get all the countries that match the given filter parameters
        countries = cls.objects.filter(**kwargs)

        # Return the queryset of countries
        return countries

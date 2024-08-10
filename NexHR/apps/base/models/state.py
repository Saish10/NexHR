__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.db import models
from django.utils.translation import gettext_lazy as _
from .base import ModelBase
from .country import ModelCountry


class ModelState(ModelBase):
    """
    State model for the application.
    """

    name = models.CharField(
        max_length=100,
        verbose_name=_("State Name"),
        help_text=_("The official name of the state or province."),
    )
    code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name=_("State Code"),
        help_text=_(
            "The code or abbreviation used for the state or province (e.g., 'CA' for California)."
        ),
    )
    country = models.ForeignKey(
        ModelCountry,
        on_delete=models.CASCADE,
        related_name="states",
        verbose_name=_("Country"),
        help_text=_("The country to which this state or province belongs."),
    )

    class Meta:
        db_table = "state"
        verbose_name = _("State")
        verbose_name_plural = _("States")
        ordering = ["name"]

    def __str__(self):
        """
        Returns a string representation of the state model object.

        The string representation is the name of the state and its country.

        :return: A string representing the state and its country.
        :rtype: str
        """
        # Construct the state representation as <state name>, <country name>
        return f"{self.name}, {self.country.name}"

    @classmethod
    def get_state(cls, **kwargs):
        """
        Returns the state with the given name and country.

        :param kwargs: A dictionary of keyword arguments to filter the state.
        :type kwargs: dict
        :return: The state with the given name and country.
        :rtype: cls
        """
        return cls.objects.get(**kwargs)

    @classmethod
    def get_states(cls, **kwargs):
        """
        Returns a queryset of states with the given name and country.

        :param kwargs: A dictionary of keyword arguments to filter the states.
        :type kwargs: dict
        :return: A queryset of states with the given name and country.
        :rtype: QuerySet
        """
        return cls.objects.filter(**kwargs)

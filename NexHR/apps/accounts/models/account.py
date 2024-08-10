__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from accounts.managers.account import UserManager
from base.models.base import ModelBase
from base.models.country import ModelCountry
from base.models.state import ModelState
from phonenumber_field.modelfields import PhoneNumberField


class ModelUser(AbstractBaseUser, PermissionsMixin, ModelBase):
    """
    User model for the application.
    """

    email = models.EmailField(
        unique=True,
        verbose_name=_("Email Address"),
        help_text=_("The user's email address, used for authentication."),
    )
    secondary_email = models.EmailField(
        blank=True,
        null=True,
        verbose_name=_("Secondary Email Address"),
        help_text=_("The user's secondary email address."),
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name=_("First Name"),
        help_text=_("The user's first name."),
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name=_("Last Name"),
        help_text=_("The user's last name."),
    )
    gender = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=(("male", "Male"), ("female", "Female"), ("other", "Other")),
        verbose_name=_("Gender"),
        help_text=_("The user's gender."),
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
        null=True,
        blank=True,
        help_text=_("The user's date of birth."),
    )
    joining_date = models.DateField(
        verbose_name=_("Joining Date"),
        null=True,
        blank=True,
        help_text=_("The date on which the user joined the organization."),
    )
    employee_id = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("Employee ID"),
        help_text=_("The user's employee ID."),
    )
    phone_number = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name=_("Phone Number"),
        help_text=_("The user's phone number, including country code."),
    )
    address_1 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Address 1"),
        help_text=_("The first line of the user's address."),
    )
    address_2 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Address 2"),
        help_text=_("The second line of the user's address."),
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("City"),
        help_text=_("The user's city."),
    )
    zip_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("Zip Code"),
        help_text=_("The user's zip code."),
    )
    state = models.ForeignKey(
        ModelState,
        on_delete=models.SET_NULL,
        related_name="users",
        verbose_name=_("State"),
        help_text=_("The user's state."),
        null=True,
    )
    country = models.ForeignKey(
        ModelCountry,
        on_delete=models.SET_NULL,
        related_name="users",
        verbose_name=_("Country"),
        help_text=_("The user's country."),
        null=True,
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Staff Status"),
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_full_name(self):
        """
        Returns the full name of the user, combining the first name and last name.
        If either of the names are None, returns an empty string.
        """
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """
        Returns a string representation of the user account model object.

        :return: A string representing the user account.
        :rtype: str
        """
        # Return the email of the user account
        return self.email

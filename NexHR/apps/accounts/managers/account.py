__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a User model with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str, optional): The password of the user. Defaults to None.
            **extra_fields (dict): Additional fields for the user model.

        Returns:
            User: The created User model.

        Raises:
            ValueError: If the email is not provided.
        """
        # Check if email is provided
        if not email:
            raise ValueError(_("The Email field must be set"))

        # Normalize the email address
        email = self.normalize_email(email)

        # Create the user model with the provided email and extra fields
        user = self.model(email=email, **extra_fields)

        # Set the password for the user
        user.set_password(password)

        # Save the user model to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email and password.

        Args:
            email (str): The email address of the superuser.
            password (str, optional): The password of the superuser. Defaults to None.
            **extra_fields (dict): Additional fields for the user model.

        Returns:
            User: The created superuser.

        Raises:
            ValueError: If the email is not provided.
        """
        # Set is_staff and is_superuser fields to True by default
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Call create_user method to create the superuser
        return self.create_user(email, password, **extra_fields)

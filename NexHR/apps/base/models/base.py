__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

import ulid
from django.db import models
from django.utils.translation import gettext_lazy as _


class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 26  # ULID string length
        kwargs["default"] = ulid.new
        kwargs["editable"] = False
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if add and not getattr(model_instance, self.attname):
            ulid_value = ulid.new().str
            setattr(model_instance, self.attname, ulid_value)
            return ulid_value
        else:
            return super().pre_save(model_instance, add)


class ModelBase(models.Model):
    """
    Base model for all models in the application.
    """

    internal_id = ULIDField(
        verbose_name=_("Internal ID"),
        help_text=_("Unique identifier for the {object_name}."),
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=True,
        help_text=_("Indicates if the {object_name} is active."),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
        help_text=_("Date and time when the {object_name} was created."),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
        help_text=_("Date and time when the {object_name} was last updated."),
        null=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        object_name = self._meta.verbose_name.lower()
        self._meta.get_field("internal_id").help_text = self._meta.get_field(
            "internal_id"
        ).help_text.format(object_name=object_name)
        self._meta.get_field("is_active").help_text = self._meta.get_field(
            "is_active"
        ).help_text.format(object_name=object_name)
        self._meta.get_field("created_at").help_text = self._meta.get_field(
            "created_at"
        ).help_text.format(object_name=object_name)
        self._meta.get_field("updated_at").help_text = self._meta.get_field(
            "updated_at"
        ).help_text.format(object_name=object_name)

    class Meta:
        abstract = True

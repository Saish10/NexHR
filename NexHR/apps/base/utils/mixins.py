__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

class FieldsMixin:
    def __init__(self, *args, **kwargs):
        only_fields = kwargs.pop("fields", None)

        super().__init__(*args, **kwargs)

        if only_fields:
            allowed = set(only_fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

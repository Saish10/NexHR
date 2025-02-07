"""
Load all fixtures
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, NexHR"

import os
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """
    Load all fixtures command
    """
    help = "Load all fixtures"

    def handle(self, *args, **options):
        # Define the fixture files to load
        fixtures = [
            "NexHR/fixtures/ModelCountry.json",
            # "/fixtures/ModelState.json",
        ]

        for fixture in fixtures:
            if os.path.exists(fixture):
                self.stdout.write(
                    self.style.SUCCESS(f"Loading fixture {fixture}")
                )
                call_command("loaddata", fixture)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Fixture file {fixture} does not exist")
                )

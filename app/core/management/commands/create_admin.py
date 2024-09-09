"""create default admin
"""

from django.core.management.base import BaseCommand
from django.db import DatabaseError
from core.models import AdminData


def check_table_exists(model_name):
    """Checks if a table for the specified model exists in the database."""

    try:
        model_name.objects.exists()
        return True
    except DatabaseError:
        return False


class Command(BaseCommand):
    """Django management command to create a default rule and admin if do not exist"""

    help = "Create a default rule and admin"

    def handle(self, *args, **kwargs):

        # * check admindata table exist
        while check_table_exists(AdminData):

            if not AdminData.objects.filter(username="palace").exists():
                # * Create a admin if it does not exist
                # AdminData.objects.create(
                #     username="palace",
                #     email="john@duran.co",
                #     last_name="duran",
                # )
                admin = AdminData(
                    username="palace",
                    email="john@duran.co",
                    last_name="duran",
                )
                admin.set_password("zxcZ@123")
                admin.save()
                self.stdout.write(
                    self.style.SUCCESS("Successfully created a new admin")
                )
            else:
                self.stdout.write(self.style.WARNING("Admin already exists"))
            break
        else:
            print("Admin table does not exist.")

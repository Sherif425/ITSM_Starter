from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        ENGINEER = "ENGINEER", "Engineer"
        HELP_DESK = "HELP_DESK", "Help Desk"
        EMPLOYEE = "EMPLOYEE", "Employee"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.EMPLOYEE,
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

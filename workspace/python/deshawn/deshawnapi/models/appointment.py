"""Appointment database model module"""
from django.db import models  # import base class from Django stdlib


class Appointment(models.Model):  # Must inherit from this base class
    """Database model for tracking walker appointments"""
    # define all non-id fields
    completed = models.BooleanField(default=False)
    date = models.DateField()
    walker = models.ForeignKey(
        'Walker', on_delete=models.CASCADE, related_name='appointments')

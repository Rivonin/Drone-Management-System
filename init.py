"""
Initialize the drone_management app and Celery setup.
"""
from __future__ import absolute_import, unicode_literals

# Import Celery app for use in other modules
from .celery import app as celery_app

__all__ = ('celery_app',)

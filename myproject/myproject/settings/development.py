"""
Settings used for local development.
"""

from .base import *


ALLOWED_HOSTS = "*"

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

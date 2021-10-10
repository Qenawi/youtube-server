"""
Settings used for running tests.
"""


CACHES = {
    "default": {
        # Use dummy cache (ie, no caching):
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

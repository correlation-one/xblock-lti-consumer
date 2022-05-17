"""
Custom testing settings for testing views
"""
from workbench.settings import *


# Usage id pattern (from edx-platform)
USAGE_ID_PATTERN = r'(?P<usage_id>(?:i4x://?[^/]+/[^/]+/[^/]+/[^@]+(?:@[^/]+)?)|(?:[^/]+))'

# Keep settings, use different ROOT_URLCONF
ROOT_URLCONF = 'test_urls'

# LMS Urls - for LTI 1.3 testing
LMS_ROOT_URL = "https://example.com"
LMS_BASE = "example.com"

# Dummy FEATURES dict
FEATURES = {}

# Set rest framework settings to test pagination
REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}

DEFAULT_HASHING_ALGORITHM = "sha1"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

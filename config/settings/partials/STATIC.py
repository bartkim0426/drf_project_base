import os

from .BASE import PROJECT_ROOT, BASE_DIR

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

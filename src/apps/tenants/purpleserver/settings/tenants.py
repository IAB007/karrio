from django.conf.global_settings import CACHES
from purpleserver.settings.base import (
    DATABASES,
    MIDDLEWARE,
    BASE_APPS,
    INSTALLED_APPS
)

DATABASES["default"]["ENGINE"] = "tenant_schemas.postgresql_backend"

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    *MIDDLEWARE,
]

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

SHARED_APPS = [
    "purpleserver.tenants",
    "tenant_schemas",

    *BASE_APPS
]

TENANT_APPS = [*INSTALLED_APPS]

INSTALLED_APPS = [
    "purpleserver.tenants",
    "tenant_schemas",

    *INSTALLED_APPS
]

TENANT_MODEL = "tenants.Client"

PUBLIC_SCHEMA_NAME = 'public'
PUBLIC_SCHEMA_URLCONF = 'purpleserver.tenants.urls'
TENANT_LIMIT_SET_CALLS = True


# Storage config
MEDIA_ROOT = '/data/media'
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

# Cache config
CACHES["default"]['KEY_FUNCTION'] = 'tenant_schemas.cache.make_key'

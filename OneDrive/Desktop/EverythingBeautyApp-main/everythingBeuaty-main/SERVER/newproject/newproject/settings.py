from pathlib import Path
from datetime import timedelta
from corsheaders.defaults import default_headers
import os

BASE_DIR = Path(**file**).resolve().parent.parent

# ========================

# SECURITY

# ========================

SECRET_KEY = os.environ.get(
"SECRET_KEY",
"django-insecure-dev-key"  # fallback for local only
)

DEBUG = os.environ.get("DEBUG", "True") == "True"

# Render hostname

RENDER_HOST = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

ALLOWED_HOSTS = [RENDER_HOST] if RENDER_HOST else ["127.0.0.1", "localhost"]

CSRF_TRUSTED_ORIGINS = (
[f"https://{RENDER_HOST}"] if RENDER_HOST else [
"http://localhost:3000",
"http://127.0.0.1:3000",
]
)

# ========================

# APPLICATIONS

# ========================

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',

```
'rest_framework',
'corsheaders',
'rest_framework_simplejwt',

'newproject',
'api.apps.ApiConfig',
```

]

MIDDLEWARE = [
'corsheaders.middleware.CorsMiddleware',
'django.middleware.security.SecurityMiddleware',

```
# Whitenoise (must be high)
'whitenoise.middleware.WhiteNoiseMiddleware',

'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
```

]

ROOT_URLCONF = 'newproject.urls'

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]

WSGI_APPLICATION = 'newproject.wsgi.application'

# ========================

# DATABASE

# ========================

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

# ========================

# PASSWORD VALIDATION

# ========================

AUTH_PASSWORD_VALIDATORS = [
{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================

# INTERNATIONALIZATION

# ========================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ========================

# STATIC FILES

# ========================

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ========================

# REST FRAMEWORK

# ========================

REST_FRAMEWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': (
'rest_framework_simplejwt.authentication.JWTAuthentication',
)
}

SIMPLE_JWT = {
"ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
"REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# ========================

# CORS

# ========================

CORS_ALLOWED_ORIGINS = [
"http://localhost:3000",
"http://127.0.0.1:3000",
]

if RENDER_HOST:
CORS_ALLOWED_ORIGINS.append(f"https://{RENDER_HOST}")

CORS_ALLOW_HEADERS = list(default_headers) + [
"Authorization",
]

CORS_ALLOW_CREDENTIALS = True

# ========================

# CSRF

# ========================

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_HTTPONLY = False

# ========================

# EMAIL (SAFE VERSION)

# ========================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ========================

# DEFAULT PK

# ========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========================

# SECURITY (PRODUCTION ONLY)

# ========================

if not DEBUG:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

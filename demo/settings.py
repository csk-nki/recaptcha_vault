"""minimal django settings for demo project."""
DEBUG = True

# Using random here for the demo, but that will change the SECRET_KEY for each
# run. For deployments consider an unique static string.
# See https://docs.djangoproject.com/en/1.5/ref/settings/#std:setting-SECRET_KEY
import random, string  # pylint: disable=W0402
SECRET_KEY = ''.join([random.choice(string.printable) for i in range(64)])

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
)
ROOT_URLCONF = 'demo.urls'
WSGI_APPLICATION = 'demo.wsgi.application'

INSTALLED_APPS = (
    'captcha',  # add dependency
    'recaptcha_vault',  # add our package
)

# For demo purpose only
# Create your own keys on http://www.google.com/recaptcha/whyrecaptcha
RECAPTCHA_PUBLIC_KEY = '6Lc5X-MSAAAAAKOfaKtKCzbzwM7t9ewxPKh4UlYf'
RECAPTCHA_PRIVATE_KEY = '6Lc5X-MSAAAAACHAgc67iNnWLyjp4lYN7rLI--MT'
RECAPTCHA_USE_SSL = True

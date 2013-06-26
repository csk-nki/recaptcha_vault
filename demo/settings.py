# minimal django settings for demo project.
DEBUG = True
SECRET_KEY = "Make this unique, and don't share it with anybody."
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

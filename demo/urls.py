from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'recaptcha_vault.views.index'),
)

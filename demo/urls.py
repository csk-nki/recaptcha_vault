from django.conf.urls import patterns, url
import demo.views

urlpatterns = patterns('',
    url(r'^.*', 'recaptcha_vault.views.protect', {'unprotected_view': demo.views.index}),
)

from django.shortcuts import render
from recaptcha_vault.forms import ReCaptchaForm

def protect(request, unprotected_view):
    """ Protect unprotected_view with recaptcha.

    If the recaptcha is valid the unprotected_view is dispatched, otherwise
    show ReCaptchaForm.
    """
    if request.method == 'POST':
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            return unprotected_view(request)
    else:
        form = ReCaptchaForm()

    return render(request, 'recaptcha_vault/form.html', {
        'form': form,
        'full_path': request.get_full_path(),
    })

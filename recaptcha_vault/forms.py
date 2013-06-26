from django import forms
from captcha.fields import ReCaptchaField

class ReCaptchaForm(forms.Form):
    """ Only purpose of this form is to ensure that a human clicks the
    submit button.
    """
    captcha = ReCaptchaField()

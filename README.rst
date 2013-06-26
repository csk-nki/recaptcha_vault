===============
recaptcha_vault
===============
Introduction
------------
A public document vault for django featuring protection againt enumeration
via recaptcha.

recaptcha_vault is a django application. Read more about Django:
https://www.djangoproject.com/

License
-------
This software is licensed under the BSD license. See LICENSE in the source
code repository.

Requirements
------------
* python2 - www.python.org
* distribute - https://pypi.python.org/pypi/distribute
* virtualenv [optional] - https://pypi.python.org/pypi/virtualenv
* pypi packages, see requirements.txt

Installation and demo
---------------------
Tested with python 2.7, git and virtualenv:
| virtualenv testenv
| cd testenv
| . bin/activate
| git clone https://github.com/csk-nki/recaptcha_vault.git
| cd recaptcha_vault
| pip install -r requirements.txt
| ./manage.py runserver

Watch the instructions from the latter command to see where the demo is
running.

Next steps
----------
* If you are new to django, try the tutorial: 
https://docs.djangoproject.com/en/1.5/intro/tutorial01/
* See testenv/recaptccha_vault/demo/settings.py for hints about which settings
you need to set for your project.

Source control management and home page
---------------------------------------
See https://github.com/csk-nki/recaptcha_vault for latest update on this
software.

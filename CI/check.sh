#!/bin/bash
. ./venv/bin/activate
pylint --rcfile=CI/pylintrc --django-settings-module=app_manager.settings ./app
pylint --disable=missing-module-docstring,missing-class-docstring,missing-function-docstring --load-plugins pylint_django --django-settings-module=app_manager.settings ./app
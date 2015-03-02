from django.apps import AppConfig


class {{ cookiecutter.app_name|replace("_", " ")|title|replace(" ", "") }}Config(AppConfig):
    name = '{{ cookiecutter.app_name }}.apps.core'

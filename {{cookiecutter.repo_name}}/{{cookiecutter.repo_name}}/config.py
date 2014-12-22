from django.apps import AppConfig


class {{ cookiecutter.repo_name|replace("_", " ")|title|replace(" ", "") }}Config(AppConfig):
    name = '{{ cookiecutter.app_name }}'

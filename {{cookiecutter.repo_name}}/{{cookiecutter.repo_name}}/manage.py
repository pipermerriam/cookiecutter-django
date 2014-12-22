#!/usr/bin/env python
import os
import sys
import dotenv

PROJECT_PATH = os.path.dirname(__file__)

dotenv.load_dotenv(os.path.join(PROJECT_PATH, ".env"))
dotenv.load_dotenv(os.path.join(PROJECT_PATH, ".env_defaults"))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.repo_name }}.settings")

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)

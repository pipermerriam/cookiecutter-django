cookiecutter-django
=======================

.. image:: https://requires.io/github/pipermerriam/cookiecutter-django/requirements.png?branch=master
     :target: https://requires.io/github/pipermerriam/cookiecutter-django/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://travis-ci.org/pipermerriam/cookiecutter-django.svg?branch=master
     :target: https://travis-ci.org/pipermerriam/cookiecutter-django?branch=master
     :alt: Build Status

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Features
---------

* For Django 1.7
* Twitter Bootstrap_ 3
* Procfile_ for deploying to Heroku
* Heroku optimized requirements
* Basic caching setup

.. _Bootstrap: https://github.com/twbs/bootstrap
.. _Procfile: https://devcenter.heroku.com/articles/procfile


Constraints
-----------

* Only maintained 3rd party libraries are used.
* PostgreSQL everywhere
* Environment variables for configuration (This won't work with Apache/mod_wsgi).


Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/pipermerriam/cookiecutter-django.git

You'll be prompted for some questions, answer them, then it will create a Django project for you.


**Warning**: After this point, change 'Piper Merriam', 'pipermerriam', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name (default is "project_name")? Reddit Clone
    repo_name (default is "repo_name")? redditclone
    author_name (default is "Your Name")? Piper Merriam
    email (default is "Your email")? pipermerriam.com
    description (default is "A short description of the project.")? A reddit clone.
    year (default is "Current year")? 2014
    domain_name (default is "Domain name")?


Enter the project and take a look around::

    $ cd redditclone/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit"
    $ git remote add origin git@github.com:pipermerriam/redditclone.git
    $ git push -u origin master

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Then, create a PostgreSQL database and add the database configuration using the  ``dj-database-url`` app pattern: ``postgres://db_owner:password@dbserver_ip:port/db_name`` either:

* in the ``config.common.py`` setting file,
* or in the env variable ``DATABASE_URL``



You can now run the usual Django ``migrate`` and ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

    $ python yourapp/manage.py migrate

    $ python yourapp/manage.py runserver

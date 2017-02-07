from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
"""
[zhaotong@bogon djangopython]$ python manage.py makemigrations
Migrations for 'front':
  front/migrations/0001_initial.py:
    - Create model Person
[zhaotong@bogon djangopython]$ python manage.py migrate
System check identified some issues:

WARNINGS:
?: (mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL,
         such as data truncation upon insertion, by escalating warnings into errors.
          It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-sql-mode
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, front, sessions
Running migrations:
  Applying front.0001_initial... OK
"""


class Person ( models.Model ) :
    name = models.CharField ( max_length = 30 )
    email = models.CharField ( max_length = 30 )
    age = models.IntegerField ( )

    def __str__ (self) :
        return self.name


@python_2_unicode_compatible
class Author ( models.Model ) :
    name = models.CharField ( max_length = 50 )
    qq = models.CharField ( max_length = 20 )
    addr = models.TextField ( )
    email = models.EmailField ( )

    def __str__ (self) :
        return self.name


@python_2_unicode_compatible
class Article ( models.Model ) :
    title = models.CharField ( max_length = 50 )
    author = models.ForeignKey ( Author )
    content = models.TextField ( )
    score = models.IntegerField ( )
    tags = models.ManyToManyField ( 'Tag' )

    def __str__ (self) :
        return self.title


@python_2_unicode_compatible
class Tag ( models.Model ) :
    name = models.CharField ( max_length = 50 )

    def __str__ (self) :
        return self.name

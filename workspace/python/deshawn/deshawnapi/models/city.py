# models: special classes to interact with the database
from django.db import models # import base class from Django stdlib


class City(models.Model): # Must inherit from this base class
    # database for cites has 2 properties: id, name
    # only name property is defined
    # bc when generate a table from database model, django automatically
    # creates the id column, makes it PK, autoincrements
    name = models.CharField(max_length=155) #define all non-id fields

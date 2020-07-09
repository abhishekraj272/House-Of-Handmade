from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Sweater(models.Model):
    name=models.TextField(blank=True,null=True)
    productcode=models.TextField(blank=True,null=True)
    soldby=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    pattern=models.TextField(blank=True,null=True)
    neck=models.TextField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)
    occasion=models.TextField(blank=True,null=True)
    washcare=models.TextField(blank=True,null=True)
    cost=models.TextField(blank=True,null=True)
    person=models.TextField(blank=True,null=True)

class Vase(models.Model):
    name=models.TextField(blank=True,null=True)
    productcode=models.TextField(blank=True,null=True)
    soldby=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    pattern=models.TextField(blank=True,null=True)
    shape=models.TextField(blank=True,null=True)
    material=models.TextField(blank=True,null=True)
    colour=models.TextField(blank=True,null=True)
    dimensions=models.TextField(blank=True,null=True)
    cost=models.TextField(blank=True,null=True)

class Sock(models.Model):
    name=models.TextField(blank=True,null=True)
    productcode=models.TextField(blank=True,null=True)
    soldby=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    length=models.TextField(blank=True,null=True)
    multipackset=models.TextField(blank=True,null=True)
    fabric=models.TextField(blank=True,null=True)
    pattern=models.TextField(blank=True,null=True)
    washcare=models.TextField(blank=True,null=True)
    cost=models.TextField(blank=True,null=True)
    person=models.TextField(blank=True,null=True)

class Scarf(models.Model):
    name=models.TextField(blank=True,null=True)
    productcode=models.TextField(blank=True,null=True)
    soldby=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    pattern=models.TextField(blank=True,null=True)
    fabric=models.TextField(blank=True,null=True)
    border=models.TextField(blank=True,null=True)
    lengthandwidth=models.TextField(blank=True,null=True)
    washcare=models.TextField(blank=True,null=True)
    cost=models.TextField(blank=True,null=True)
    person=models.TextField(blank=True,null=True)

class Earring(models.Model):
    name=models.TextField(blank=True,null=True)
    productcode=models.TextField(blank=True,null=True)
    soldby=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    shape=models.TextField(blank=True,null=True)
    basemetal=models.TextField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)
    occasion=models.TextField(blank=True,null=True)
    closure=models.TextField(blank=True,null=True)
    multipackset=models.TextField(blank=True,null=True)
    cost=models.TextField(blank=True,null=True)
    person=models.TextField(blank=True,null=True)
    sizeandfit=models.TextField(blank=True,null=True)
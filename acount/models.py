# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acount(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    count = models.IntegerField()
    unit = models.CharField(max_length=10)
    price = models.IntegerField()
    sumprice = models.IntegerField()
    tax = models.IntegerField()
    totalprice = models.IntegerField()
    inoutcompany = models.CharField(max_length=50, blank=True, null=True)
    incomeprice = models.IntegerField(blank=True, null=True)
    division = models.CharField(max_length=10, blank=True, null=True)
    paymethod = models.CharField(max_length=45, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acount'

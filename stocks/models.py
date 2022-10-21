# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from products.models import Products


class Stocks(models.Model):
    idstocks = models.AutoField(primary_key=True)
    idproducts = models.ForeignKey(Products, related_name='pstock', on_delete=models.DO_NOTHING, db_column='idproducts')
    date = models.DateField()
    category = models.CharField(max_length=45)
    p_name = models.CharField(max_length=45)
    company = models.CharField(max_length=45)
    in_field = models.IntegerField(blank=True, null=True)
    out_field = models.IntegerField(blank=True, null=True)
    return_field = models.IntegerField(blank=True, null=True)
    lost_field = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=45)
    remark = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stocks'

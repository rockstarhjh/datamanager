from django.db import models


# Create your models here.

class Products(models.Model):
    idproducts = models.AutoField(primary_key=True)
    category = models.CharField(max_length=45, db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    p_name = models.CharField(max_length=45, db_collation='utf8mb4_unicode_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'

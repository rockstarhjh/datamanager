from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30)
    comnum = models.CharField(max_length=30, blank=True, null=True)
    ceo = models.CharField(max_length=30, blank=True, null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=30, blank=True, null=True)
    delivery = models.CharField(max_length=200, blank=True, null=True)
    cellphone = models.CharField(max_length=30, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    division = models.CharField(max_length=10, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'

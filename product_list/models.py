from __future__ import unicode_literals
from django.db import models


class CheckList(models.Model):
    STATUSES = (('P', "Pending"), ('D', 'Done'))
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUSES)
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class ListItem(models.Model):
    check_list = models.ForeignKey(CheckList)
    STATUSES = (('P', "Pending"), ('D', 'Done'), ('R', "Reject"))
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUSES)

    def __unicode__(self):
        return self.name


class ListItemDescription(models.Model):
    STATUSES = (('P', "Pending"), ('D', 'Done'), ('R', "Reject"))
    QUANTITY_UNITS = (('K', "KG"), ('P', 'Pack'), ('L', 'Liter'), ('M', 'Meter'))
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    quantity = models.FloatField(default=0.0)
    quantity_units = models.CharField(max_length=1, choices=QUANTITY_UNITS)
    expected_price = models.FloatField(default=0.0)
    actual_price = models.FloatField(default=0.0)
    status = models.CharField(max_length=1, choices=STATUSES)

    def __unicode__(self):
        return self.name


class ItemToItemDescription(models.Model):
    item_description_id = models.ForeignKey(ListItemDescription)
    custom_item_id = models.ForeignKey(ListItem)

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Investor(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)
    name = models.CharField(max_length=100, unique=True)
    percent = models.IntegerField(default=0)
    sum = models.FloatField(default=0)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return "%s: %s, %s (%s)" % (self.pk, self.name, self.sum, self.percent)

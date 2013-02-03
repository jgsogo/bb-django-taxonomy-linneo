#!/usr/bin/env python
# encoding: utf-8

from django.db import models

class TaxonRankMixin(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    in_rank_order = models.IntegerField(default=0)
    compulsory = models.BooleanField(default=False)

    class Meta:
        ordering = ['rank', 'in_rank_order']
        abstract = True

    def __unicode__(self):
        return self.name


class TaxonMixin(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def get_name(self):
        return self.taxon_name

    def save(self, *args, **kwargs):
        """ Only 'domains' can be orphans, everything else must be included in a supracategory """
        #if self.rank != '':
        #    raise

        """ Parent also must be in the same rank (parent.in_rank_order > self.in_rank_order) or in a higher rank """
        super(TaxonMixin, self).save(*args, **kwargs)

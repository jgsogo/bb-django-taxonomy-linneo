#!/usr/bin/env python
# encoding: utf-8

from django.db import models

from taxonomy.models import Taxon, TaxonRank

# Major ranks Linneo
from linneo.managers import MajorTaxonomicRankManager

class RankFromMixin(object):
    def save(self, *args, **kwargs):
        self.rank = self.__class__.objects._get_rank()
        super(RankFromMixin, self).save(*args, **kwargs)


class DomainTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(0, "domain")
    class Meta:
        proxy = True

class KingdomTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(0, "kingdom")
    class Meta:
        proxy = True

class PhylumTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(1, "phylum-division")
    class Meta:
        proxy = True

class ClassTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(3, "class")
    class Meta:
        proxy = True

class OrderTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(7, "order")
    class Meta:
        proxy = True

class FamilyTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(9, "family")
    class Meta:
        proxy = True

class GenusTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(11, "genus")
    class Meta:
        proxy = True

class SpeciesTaxon(RankFromMixin, Taxon):
    objects = MajorTaxonomicRankManager(12, "species")
    class Meta:
        proxy = True

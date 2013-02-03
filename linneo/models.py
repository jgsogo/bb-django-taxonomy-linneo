#!/usr/bin/env python
# encoding: utf-8

from django.db import models

from taxonomy.models import Taxon
from linneo.managers import MajorTaxonomicRankManager

class DomainTaxon(Taxon):
    objects = MajorTaxonomicRankManager(0, "domain")
    class Meta:
        proxy = True

class KingdomTaxon(Taxon):
    objects = MajorTaxonomicRankManager(0, "kingdom")
    class Meta:
        proxy = True

class PhylumTaxon(Taxon):
    objects = MajorTaxonomicRankManager(1, "phylum-division")
    class Meta:
        proxy = True

class ClassTaxon(Taxon):
    objects = MajorTaxonomicRankManager(3, "class")
    class Meta:
        proxy = True

class OrderTaxon(Taxon):
    objects = MajorTaxonomicRankManager(7, "order")
    class Meta:
        proxy = True

class FamilyTaxon(Taxon):
    objects = MajorTaxonomicRankManager(9, "family")
    class Meta:
        proxy = True

class GenusTaxon(Taxon):
    objects = MajorTaxonomicRankManager(11, "genus")
    class Meta:
        proxy = True

class SpeciesTaxon(Taxon):
    objects = MajorTaxonomicRankManager(12, "species")
    class Meta:
        proxy = True


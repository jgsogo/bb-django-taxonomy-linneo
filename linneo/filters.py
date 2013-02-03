#!/usr/bin/env python
# encoding: utf-8

from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

from taxonomy.models import TaxonRank

class RankListFilter(SimpleListFilter):
    title = _('taxonomic rank')

    parameter_name = 'taxo_rank'

    def lookups(self, request, model_admin):
        return (
            ('0', _('kingdom-group ranks')),
            ('1', _('phylum-group ranks')),
            ('2', _('cohort(botany)-group ranks')),
            ('3', _('class-group ranks')),
            ('4', _('division(zoology)-group ranks')),
            ('5', _('legion-group ranks')),
            ('6', _('cohort(zoology)-group ranks')),
            ('7', _('order-group ranks')),
            ('8', _('section-group ranks')),
            ('9', _('family-group ranks')),
            ('10', _('tribe-group ranks')),
            ('11', _('genus-group ranks')),
            ('12', _('species-group ranks')),
            )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(rank__rank=self.value())
        else:
            return queryset.all()

class InRankListFilter(SimpleListFilter):
    title = _('minorrank filter')
    parameter_name = 'minortaxo_rank'

    def lookups(self, request, model_admin):
        rank = model_admin.model.objects._get_rank().rank
        return ( (it.in_rank_order, it) for it in TaxonRank.objects.filter(rank=rank))

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(rank__in_rank_order=self.value())
        else:
            return queryset.all()

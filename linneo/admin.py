#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin

from taxonomy.admin import TaxonAdmin
from linneo.models import DomainTaxon, KingdomTaxon
from linneo.filters import RankListFilter, InRankListFilter

class MajorTaxonomicRankAdmin(TaxonAdmin):
    exclude = ('rank',)
    list_display = ('name', 'rank',)
    mptt_level_indent = 20
    list_filter = ()

admin.site.register(DomainTaxon, MajorTaxonomicRankAdmin)
admin.site.register(KingdomTaxon, MajorTaxonomicRankAdmin)


# Override Taxon admin to provide filtering
from taxonomy.models import Taxon
admin.site.unregister(Taxon)

class TaxonAdmin(TaxonAdmin):
    list_display = ('name', 'rank',)
    list_filter = (RankListFilter, InRankListFilter)
    mptt_level_indent = 20

admin.site.register(Taxon, TaxonAdmin)
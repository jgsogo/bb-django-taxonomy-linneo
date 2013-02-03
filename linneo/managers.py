#!/usr/bin/env python
# encoding: utf-8

from taxonomy.managers import TaxonManager
from taxonomy.models import TaxonRank

class MajorTaxonomicRankManager(TaxonManager):
    def __init__(self, rank, slug):
        super(MajorTaxonomicRankManager, self).__init__()
        self.__rank__rank = rank
        self.__slug = slug
        self.__rank = None

    def _get_rank(self):
        try:
            self.__rank = TaxonRank.objects.get(rank=self.__rank__rank, slug=self.__slug)
        except TaxonRank.ObjectDoesNotExist:
            raise ValueError("Couldn't find a taxon rank named %s (rank=%s)." %\
                             (self.__rank__rank, self.__slug))
        except TaxonRank.MultipleObjectsReturned:
            raise ValueError("There are more than one taxon rank named %s (rank=%s)." %\
                             (self.__rank__rank, self.__slug))
        return self.__rank

    def get_query_set(self):
        if not self.__rank:
            self._get_rank()
        return super(MajorTaxonomicRankManager, self).get_query_set().filter(rank=self.__rank)


class TaxonomicRankGroupManager(TaxonManager):
    def __init__(self, rank):
        super(TaxonomicRankGroupManager, self).__init__()
        self.__rank= rank

    def get_query_set(self):
        return super(TaxonomicRankGroupManager, self).get_queryset().filter(rank__rank=self.__rank)

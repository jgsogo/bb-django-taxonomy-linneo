#!/usr/bin/env python
# encoding: utf-8

from taxonomy.managers import TaxonManager


class DominioManager(TaxonManager):
    def get_query_set(self):
        return super(DominioManager, self).get_query_set().filter()
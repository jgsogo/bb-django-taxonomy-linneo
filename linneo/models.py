#!/usr/bin/env python
# encoding: utf-8

from django.db import models

from taxonomy.models import Taxon


class Dominio(Taxon):

    class Meta:
        proxy = True

class Reino(Taxon):

    class Meta:
        proxy = True


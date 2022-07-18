from django.db import models


class MetaTable(models.Model):
    pass


class GeneTable(models.Model):
    gene_name = models.TextField()
    sequence = models.TextField()


class StructTable(models.Model):
    pass



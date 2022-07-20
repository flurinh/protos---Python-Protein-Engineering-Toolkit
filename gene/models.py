from django.db import models

# Create your models here.

class GeneTable(models.Model):
    gene_name = models.TextField(primary_key=True)
    sequence = models.TextField(1500)
from django.db import models

# Create your models here.

class GRNTable(models.Model):
    # make the gene names unique
    # allow for multiple annotation schemes? => how?
    gene_name = models.TextField(primary_key=True)
    scheme = models.TextField()

from django.db import models

# Create your models here.

class StructTable(models.Model):
    struct_name = models.TextField(primary_key=True)
    gene_name = models.TextField()
    res_type = models.TextField()
    atom_type = models.TextField()
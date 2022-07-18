from django.db import models


class Selections(models.Model):
    selection_nr = models.IntegerField()
    selection_owner = models.ForeignKey('TestUser', on_delete=models.SET_NULL, null=True)
    """
    CASCADE will propagate the change when the parent changes. (If you delete a row, rows 
    in constrained tables that reference that row will also be deleted, etc.)

    SET NULL sets the column value to NULL when a parent row goes away.

    RESTRICT causes the attempted DELETE of a parent row to fail.
    """
    use_gene_info = models.BooleanField()
    use_grn_info = models.BooleanField()
    use_struct_info = models.BooleanField()




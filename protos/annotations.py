from django.db import models




class Annotations(models.Model):
    annotation_nr = models.IntegerField()
    annotation_owner = models.ForeignKey('TestUser', on_delete=models.SET_NULL, null=True)
    # which_table_is_annotated = models.IntegerField()  # Polymorphic Associations => use joins
    annotation = models.TextField(max_length=500)



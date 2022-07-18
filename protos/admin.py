from django.contrib import admin

# Register your models here.

from .models import TestUser, Selections, GeneTable

admin.site.register(TestUser)
admin.site.register(Selections)
admin.site.register(GeneTable)
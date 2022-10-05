from django.contrib import admin
from .models import Crud
# Register your models here.

class CrudAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'updated_at')
    fields = ['title', 'content']

admin.site.register(Crud, CrudAdmin)

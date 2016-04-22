from django.contrib import admin
from .models import CheckList,ListItem

class ListItemInline(admin.TabularInline):
    model = ListItem
    extra=3

class CheckListAdmin(admin.ModelAdmin):
    fields = ['pub_date','title','status']
    inlines = [ListItemInline]

admin.site.register(CheckList,CheckListAdmin)


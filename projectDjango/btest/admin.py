from django.contrib import admin
from .models import *
# Register your models here.


class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'price', 'rubric', 'published')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content', 'price', 'published')

class RubricAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_display_links = ('name',)
  search_fields = ('name',)

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
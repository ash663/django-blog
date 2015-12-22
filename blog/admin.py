from django.contrib import admin
from blog.models import *

class PostsAdmin(admin.ModelAdmin):
    search_fields=["title"]
    display_fields = "title created category".split()

class CommAdmin(admin.ModelAdmin):
    searchfields = "title author".split()
    display_fields = "title author created".split()

admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommAdmin)
# Register your models here.

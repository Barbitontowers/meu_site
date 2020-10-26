from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created", "updated","status")
    list_filter = ('status','title','author','created')
    date_hierarchy = 'publish'
    search_fields = ('author',)
    prepopulated_fields = {"slug": ("title",)}
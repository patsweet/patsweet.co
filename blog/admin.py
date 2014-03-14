from django.contrib import admin
from .models import Post, Category
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


class FlatPageCustom(FlatPageAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/TinyMCEAdmin.js'
        ]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)


class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category', 'pub_date', 'published')
    list_editable = ['category', 'published']
    list_filter = ('published',)
    search_fields = ['headline']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {"slug": ("headline",)}
    actions = ['unpublish_post']

    def unpublish_post(self, request, queryset):
        queryset.update(published=False)
    unpublish_post.short_description = "Mark selected posts as unpublished"

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/TinyMCEAdmin.js'
        ]

admin.site.register(Post, PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)

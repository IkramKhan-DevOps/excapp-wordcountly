from django.contrib import admin
from .models import (
    BlogCategory, BlogTag, Blog, Content
)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'read_time', 'is_active', 'created_on', 'updated_on']
    list_filter = ['category', 'tags']
    search_fields = ['title']
    readonly_fields = ['created_on', 'updated_on']
    fieldsets = (
        (None, {'fields': ('title', 'thumbnail')}),
        ('Relation', {'fields': ('category', 'tags')}),
        ('Content', {'fields': ('description', 'content')}),
        ('Statistics', {'fields': ('read_time',)}),
        ('Permissions', {
            'fields': ('is_active',),
        }),
        ('Important dates', {'fields': ('created_on', 'updated_on')}),
    )


class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'base_url', 'lat', 'long', 'created_on']
    readonly_fields = ['created_on']
    fieldsets = (
        (None, {'fields': ('name', 'tagline', 'base_url')}),
        ('Images', {'fields': ('favicon_icon', 'logo')}),
        ('Contact', {'fields': ('contact_phone', 'contact_email')}),
        ('Location', {'fields': ('address', 'lat', 'long')}),
        ('Privacy Policy', {'fields': ('privacy_policy',)}),
        ('Important dates', {'fields': ('created_on',)}),
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)

from django.contrib import admin
from gallery.models import Album, ImageInAlbum


class ImageInAlbumInline(admin.TabularInline):
    model = ImageInAlbum
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInAlbumInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'image', 'date')
        }),
        ('SEO', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug', 'seo_title', 'desc', 'keywords'),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
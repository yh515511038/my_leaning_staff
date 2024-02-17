from django.contrib import admin
from django.utils.safestring import SafeString
from imagekit.admin import AdminThumbnail
from imagekit.processors import ResizeToFit
from .models import BanBan

# Register your models here.
class ResizedAdminThumbnail(AdminThumbnail):
    # Resize the thumbnail to the desired dimensions
    def __call__(self, obj):
        thumbnail_html = super().__call__(obj)
        thumbnail_html_image = thumbnail_html.replace('<img', '<img width="100" height="133"')
        return SafeString(thumbnail_html_image)


class BanBanAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_resized_thumbnail')
    admin_resized_thumbnail = ResizedAdminThumbnail(image_field='image')


admin.site.register(BanBan, BanBanAdmin)

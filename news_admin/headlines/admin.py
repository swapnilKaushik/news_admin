from django.contrib import admin

from .models import Headline, HeadlineImage, HeadlineVideo


class HeadlineImageInline(admin.TabularInline):
    model = HeadlineImage


class HeadlineVideoInline(admin.TabularInline):
    model = HeadlineVideo


@admin.register(Headline)
class HeadLineAdmin(admin.ModelAdmin):
    inlines = [HeadlineImageInline, HeadlineVideoInline]


admin.site.register(HeadlineImage)
admin.site.register(HeadlineVideo)

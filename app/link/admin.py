from django.contrib import admin

from app.link.models import Domain, Link


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('host', 'status')
    list_filter = ('status',)
    search_fields = ('host',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    # TODO-2: add owner to list display
    list_display = ('domain', 'slug', 'url', 'visitor_limit', 'expire_time')
    search_fields = ('domain', 'slug', 'url', 'visitor_limit')

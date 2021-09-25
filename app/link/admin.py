from django.contrib import admin

from link.models import Domain, Link


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('host', 'status')
    list_filter = ('status',)
    search_fields = ('host',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain', 'slug', 'url', 'visitor_limit', 'expire_time')
    search_fields = ('domain', 'slug', 'url', 'visitor_limit')

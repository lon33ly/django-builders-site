from django.contrib import admin
from .models import Projects, Team, ContactBadges, IndexBadges, Requests
from django.utils.html import mark_safe


# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'location')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="120" height="80"')

    get_image.short_description = "Изображение"


class TeamAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'position', 'description')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="120" height="80"')

    get_image.short_description = "Изображение"


class IndexBadgesAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="80" height="80"')

    get_image.short_description = "Изображение"


class ContactBadgesAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="80" height="80"')

    get_image.short_description = "Изображение"


class RequestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(IndexBadges, IndexBadgesAdmin)
admin.site.register(ContactBadges, ContactBadgesAdmin)
admin.site.register(Requests, RequestsAdmin)
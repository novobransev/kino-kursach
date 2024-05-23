from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo}" width="100" />')
        else:
            return '-'
    photo_preview.short_description = 'Фото'


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo_preview')

    def photo_preview(self, obj):
        if obj.poster:
            return mark_safe(f'<img src="{obj.poster}" width="100" />')
        else:
            return '-'
    photo_preview.short_description = 'Фото'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', "text")


admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
admin.site.register(Actor, ActorAdmin)

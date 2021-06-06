from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html

from project.core.models import Speaker, Contact


class ContactInLine(admin.TabularInline):
    model=Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'photo_img', 'website_link']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'foto'



admin.site.register(Speaker, SpeakerModelAdmin)
# class SpeakerModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug', 'website', 'photo', 'description')
#     # date_hierarchy = 'created_at'
#     # search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
#     # list_filter = ('paid', 'created_at')
#
# admin.site.register(Speaker, SpeakerModelAdmin)
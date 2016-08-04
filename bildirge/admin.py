from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser, Doc, Contact



class ContactAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","updated"]
    class Meta:
        model = Contact
admin.site.register(Contact, ContactAdmin)


class DocAdmin(admin.ModelAdmin):
    class Meta:
        model = Doc

admin.site.register(Doc, DocAdmin)
"""


class ContactInline(admin.StackedInline):
    model = Contact



class DocAdmin(admin.ModelAdmin):
    inlines = [ContactInline]



admin.site.register(Doc, DocAdmin)



from models import News, NewsLang

class NewsLangInline(admin.TabularInline):
    model = NewsLang

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsLangInline]
admin.site.register(News, NewsAdmin)"""
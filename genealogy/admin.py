from django.contrib import admin
from .models import FamilyMember

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'suffix', 'maiden_name', 'birthday', 'died_on', 'sex', 'father', 'mother', 'id')
    list_filter = ('last_name', 'sex')
    search_fields = ['last_name', 'first_name', 'maiden_name']
    date_hierarchy = 'birthday'
    raw_id_fields = ('mother', 'father')

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/TinyMCEAdmin.js'
        ]

admin.site.register(FamilyMember, FamilyMemberAdmin)

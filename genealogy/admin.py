from django.contrib import admin
from .models import FamilyMember

class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'suffix', 'maiden_name', 'birthday', 'died_on', 'sex', 'father', 'mother', 'id')
    list_filter = ('last_name', 'sex')
    search_fields = ['last_name', 'first_name', 'maiden_name']
    date_hierarchy = 'birthday'
    raw_id_fields = ('mother', 'father')

admin.site.register(FamilyMember, FamilyMemberAdmin)

from django.contrib import admin
from .models import Page , CompanyAddress


class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    search_fields = ('title' ,)
    ordering = ('title',)


admin.site.register(Page , PageAdmin)




class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name','city','state','country')
    search_fields = ('city','state','country')
    ordering = ('city',)


admin.site.register(CompanyAddress , CompanyAdmin)







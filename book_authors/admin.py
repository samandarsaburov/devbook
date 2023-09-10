from django.contrib import admin
from .models import GenreModel, AutherModel, BookModel
# from modeltranslation.admin import TranslationAdmin
# Register your models here.

# Genre admin
admin.site.register(GenreModel)


#  Auther admin
class AutherAdmin(admin.ModelAdmin):
    # pass
    list_display= ['first_name','last_name','date_of_brth','place_of_birth','date_of_death','place_of_death','images','bio','genre','user']
    search_fields = ['first_name','']
    
admin.site.register(AutherModel, AutherAdmin)


# Book Model adminss
class BookAdmin(admin.ModelAdmin):
    # pass
    list_display = ['title','pages','year','price','genre','images','auther','bio','user']
    search_fields = ['title','auther','genre']
admin.site.register(BookModel,BookAdmin)
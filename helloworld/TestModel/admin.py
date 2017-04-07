from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.

class TagInline(admin.TabularInline):
	model=Tag

class ContactAdmin(admin.ModelAdmin):
	inlines=[TagInline] #Inline
	fieldsets=(
		['Main',{'fields':('name','email'),}],
		['Advance',{'classes':('collapse',),	#css
								'fields':('age',),}]
	)
	list_display=('name','age','email') #list
	search_fields=('name',)
	
admin.site.register(Contact,ContactAdmin)
admin.site.register(Test)

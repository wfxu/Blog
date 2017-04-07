from django.contrib import admin
from models import Mes,Blog,Category,State,Log

# Register your models here.
class MesAdmin(admin.ModelAdmin):
	list_display=('message','mestime',)
	
class BlogAdmin(admin.ModelAdmin):
	list_display=('topic','toptime',)


admin.site.register(Mes,MesAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register([Category,State,Log])
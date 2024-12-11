from django.contrib import admin
from tdapp.models import Todo
# Register your models here.
class tdadmin(admin.ModelAdmin):
    list_display=['task']
admin.site.register(Todo,tdadmin)
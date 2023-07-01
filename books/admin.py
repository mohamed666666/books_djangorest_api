from django.contrib import admin

# Register your models here.
from .models import Books ,Pages

admin.site.register(Books)
admin.site.register(Pages)

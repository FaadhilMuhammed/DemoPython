from django.contrib import admin

from . models import Place
from . models import Face
# Register your models here.
admin.site.register(Place),
admin.site.register(Face)
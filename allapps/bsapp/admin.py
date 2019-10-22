from django.contrib import admin
from .models import Language, Framework


# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    pass


class FrameworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)
admin.site.register(Framework, FrameworkAdmin)

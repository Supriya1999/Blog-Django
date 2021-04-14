from django.contrib import admin
from .models import Blog,Category


# Register your models here.

@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',) , }

admin.site.register(Category)

from django.contrib import admin

from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ("name", "slug", "created", "updated")
	prepopulated_fields =  {"slug": ("name",)}

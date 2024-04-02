
from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('create_date','update_date')

admin.site.register(Article)
admin.site.register(Category)

title = "Blog de Articulos"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión"
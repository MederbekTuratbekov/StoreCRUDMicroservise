from django.contrib import admin
from .models import Category, SubCategory, ProductImage, Review, Product
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class SubCategoryInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = SubCategory
    extra = 1


# ИЗМЕНЕНО: убраны внешние http-ссылки на устаревшие jQuery/jQuery UI (2013 год).
# modeltranslation сам подключает нужный jQuery через свою статику (admin/js/vendor/jquery/jquery.js),
# который уже загружен стандартной админкой Django. Внешние копии были лишними,
# грузились по небезопасному http:// и могли блокироваться браузером как mixed content.
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    inlines = [SubCategoryInline]

    class Media:
        js = (
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageInline]

    class Media:
        js = (
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Review)

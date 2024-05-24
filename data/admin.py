from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.safestring import mark_safe
from .models import *


class ProductFeatureInline(NestedStackedInline):
    model = ProductFeature
    extra = 0


class ProductAdmin(NestedModelAdmin):
    model = Product
    inlines = [ProductFeatureInline]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):

        if obj.image:
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return 'Нет изображения'

    image_preview.short_description = 'Текущее изображение'


class ModelImageInline(NestedStackedInline):
    model = ModelImage
    extra = 0

class ModelTabInline(NestedStackedInline):
    model = ModelTab
    extra = 0

class ModelFeatureInline(NestedStackedInline):
    model = ModelFeature
    extra = 0



class ModelAdmin(NestedModelAdmin):
    model = Model
    list_display = ('image_preview','name',)
    readonly_fields = ['image_preview']
    inlines = [ModelImageInline, ModelTabInline,ModelFeatureInline]
    fields = [
        'image_preview',
        'categories',
        'is_active',
        'name',
        'name_alt',
        'slug',
        'price',
        'price_alt',
        'scheme',
        'description',
        'description_alt',
        'short_description',
        'short_description_alt',
        'tag_title',
        'tag_title_alt',
        'tag_description',
        'tag_description_alt'
    ]

    def image_preview(self, obj):
        if obj.images.all().filter(is_main=True):
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.images.all().filter(is_main=True).first().image.url))
        else:
            return 'Нет изображения'

    image_preview.short_description = 'Текущее изображение'

class CallbackFormAdmin(NestedModelAdmin):
    model = CallbackForm
    list_display = ('name',
'email',
'phone',
'subject',
'created_at',)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Faq)
admin.site.register(CallbackForm, CallbackFormAdmin)
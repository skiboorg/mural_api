from django.db import models
from django_resized import ResizedImageField
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.files import File
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True)
    old_id = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        #ordering = ('order_num',)
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'


class Model(models.Model):
    is_active = models.BooleanField('Отображать?', default=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                                 help_text='Если не заполнено, создается на основе поля Назавание',
                                 blank=True, null=True)


    description = RichTextUploadingField('Описание', blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        #ordering = ('order_num',)
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ModelTab(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='tabs')
    label = models.CharField('Название таба', max_length=255, blank=False, null=True)
    text = RichTextUploadingField('Текст', blank=True, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Таб модели'
        verbose_name_plural = 'Табы модели'

class ModelImage(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='images')
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='model/images',
                              blank=False, null=True)
    imageThumb = models.ImageField(upload_to='product/gallery/', blank=True, null=True, editable=False)
    is_main = models.BooleanField('Основная картинка', default=False)

    def __str__(self):
        return f''

    def save(self, *args, **kwargs):
        from .services import create_thumb
        self.imageThumb.save(f'{self.model.slug}-thumb.jpg', File(create_thumb(self.image)), save=False)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('is_main',)
        verbose_name = 'Картинка модели'
        verbose_name_plural = 'Картинки модели'



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False,related_name='products')
    model = models.ManyToManyField(Model, null=True, blank=True, related_name='products')
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='model/images',
                              blank=False, null=True)
    vendor_code = models.CharField('Код', max_length=255, blank=False, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True)
    description = RichTextUploadingField('Текст', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='features')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)


    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
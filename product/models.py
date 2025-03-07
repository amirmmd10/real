from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self' ,blank=True , null=True ,verbose_name=_('parent') , on_delete=models.CASCADE  )
    title =models.CharField(_('title'),max_length=55, default='Untitled Category')
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True , upload_to="categories")
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_(' updated_time'),auto_now=True)
    
    class Meta:
        db_table='categories'
        verbose_name=_('Category')
        verbose_name_plural=_('Categories')

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title =models.CharField(_('title'),max_length=55 ,default='Untitled File')
    description = models.TextField(_('description'),blank=True)
    avatar = models.ImageField(_('avatar'),blank=True , upload_to="categories")
    categories = models.ManyToManyField('Category',verbose_name=_('categories '),blank=True)
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_(' updated_time'),auto_now=True)
    
    class Meta:
        db_table='products'
        verbose_name=_('product')
        verbose_name_plural=_('products')


class File(models.Model):

    product = models.ForeignKey('Product' , verbose_name=_('product') , on_delete=models.CASCADE )
    title =models.CharField(_('title'),max_length=55 ,default='Untitled File')
    description = models.TextField(_('description'),blank=True)
    file = models.FileField(_('file'),upload_to='files/%Y/%m/%d' )
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_time = models.DateTimeField(_(' updated_time'),auto_now=True)
    
    class Meta:
        db_table='files'
        verbose_name=_('File')
        verbose_name_plural=_('Files')

  
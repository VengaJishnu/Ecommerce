from django.db import models
from django.urls import reverse


# Create your models here.

class categoty(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, max_length=250)
    # slug is to create url new one
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    # def get_url(self):
    #     return reverse('ecommerce:proCatdetail', args=[self.category.slug,self.slug])
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('ecommerce:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)  # slug will create based as per the name
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(categoty, on_delete=models.CASCADE)
    #     foreign key is used for to take the coloumns from another table to
    #    required table
    # cascade to delete the [revious data
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # this will add the created first time
    updated = models.DateTimeField(auto_now=True)  # this commadn always it will change when ever we change the content

    def get_url(self):
        return reverse('ecommerce:proCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)

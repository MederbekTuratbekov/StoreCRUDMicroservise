from django.db import models


class Category(models.Model):
    category_image = models.ImageField(upload_to='category_photo')
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_categories')

    def __str__(self):
        return f'{self.category},{self.subcategory_name}'

class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='products')
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    article_number = models.PositiveIntegerField(unique=True, verbose_name='Артикул')
    description = models.TextField()
    product_type = models.BooleanField()
    video = models.FileField(upload_to='product_videos/', null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
       ratings = self.reviews.all()
       if ratings.exists():
           return round(sum([i.stars for i in ratings]) / ratings.count(), 1)
       return 0

    def get_count_people(self):
        return self.reviews.count()


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_img')

    def __str__(self):
        return f'{self.product},{self.image}'


class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    user_id = models.IntegerField()
    stars = models.PositiveIntegerField(choices=[ (i, str (i))for i in range (1,6)])
    comment  = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.product},{self.stars}'
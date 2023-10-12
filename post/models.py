from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class specialshop(models.Model):
    title = models.CharField(max_length=150,verbose_name='Bashliq')
    subtitle = models.CharField(max_length=150, verbose_name='Alt bashliq')
    link = models.TextField(verbose_name='Url')
    image = models.ImageField(upload_to='special/')

    def __str__(self):
        return self.title




class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='Kateqoriya adı')
    bg_image = models.FileField(verbose_name='Fon(Arxa) şəkli')
    icon = models.FileField(verbose_name='Ikon şəkli', blank=True,null=True)
    image = models.FileField(verbose_name='Şəkil')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Kateqoriyası')
    name = models.CharField(max_length=100, verbose_name='Məhsulun adı')
    price = models.FloatField(verbose_name='Qiyməti')
    about = models.TextField(verbose_name='Haqqında',blank=True, null=True)
    discount = models.IntegerField(verbose_name='Endirim faizi')
    credit = models.BooleanField(verbose_name='kredit',default=False)
    garanty = models.IntegerField(verbose_name='Zəmanət',default=12)
    rating = models.FloatField(verbose_name='Reytinq',default=5)
    
    date = models.DateTimeField(auto_now_add=True)

    @property
    def dis_price(self):
        if self.discount > 0:
            dis_amount = (self.discount/100)*self.price
            final_price = self.price - dis_amount
            return final_price
        else:
            return self.price


    def __str__(self):
        return self.name
    @property
    def get_url(self):
        return reverse('detail', kwargs={'id':self.id})
    
class images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='shekli',upload_to='product/')

    def __str__(self):
        return self.product.name
    



class Phone(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Məhsulun adı')
    display = models.FloatField(verbose_name='Ekran ölçüsü')
    main_cam = models.IntegerField(verbose_name='Əsas kamera',blank=True,null=True)
    add_cam = models.IntegerField(verbose_name='Ön kamera',blank=True, null=True)
    battery = models.IntegerField(verbose_name='Batareya(mAH)')
    biometric = models.BooleanField(verbose_name='Üz tanıma')
    memory = models.IntegerField(verbose_name='Yaddaş')
    ram = models.IntegerField(verbose_name='Operativ yaddaş')
    network = models.CharField(max_length=100,verbose_name='Şəbəkə')
    COLOR = (
        ('Ağ','Ağ'),
        ('Qara','Qara'),
        ('Mavi','Mavi')
    )
    color = models.CharField(max_length=100,verbose_name='Rəngi',choices=COLOR)

    def __str__(self):
        return self.product.name
    

class Notebook(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Məhsulun adı')
    memory = models.IntegerField(verbose_name='Yaddaş')
    ram = models.IntegerField(verbose_name='Operativ yaddaş')
    COLOR = (
        ('Ağ','Ağ'),
        ('Qara','Qara'),
        ('Mavi','Mavi')
    )
    color = models.CharField(max_length=100,verbose_name='Rəngi',choices=COLOR)
    speed = models.FloatField(verbose_name='Suret(Ghz)')
    processor = models.CharField(max_length=100)
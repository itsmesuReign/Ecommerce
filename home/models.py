
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    device = models.CharField(max_length=200, null=True, blank=True )

    def __str__(self):
        return self.name


#Man
class Man(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="man_img/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


#Woman
class Women(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="women_img/")

    def __str__(self):
        return self.title


#Kids
class Kid(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="kids_img/")

    def __str__(self):
        return self.title

#Brand
class Brand(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="brand_img/")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Accessories(models.Model):

    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="accessories_img/", null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Size(models.Model):

    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

#Category
class Category(models.Model):
    slug = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="brand_img/", null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




#Product model
class Product(models.Model):

    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, blank=True)
    detail = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=7)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_man = models.BooleanField(default=False)
    is_women = models.BooleanField(default=False)
    is_kid = models.BooleanField(default=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        if self.customer==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        # return self.customerName
        return str(self.customer)

    @property
    def get_cart_subtotal(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

        

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added =  models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def get_total(self):

        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


class Ordered(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added =  models.DateTimeField(auto_now_add=True)
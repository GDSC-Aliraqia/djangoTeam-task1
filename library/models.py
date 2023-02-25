from django.db import models

# Create your models here.
class Auth(models.Model):
    A_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Section(models.Model):
    Ca_id = models.AutoField(primay_key=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField()


class Product(models.Model):
    CATEGORY_CHOICES = (
        "Scientific",
        "art",
        "historic",
        "Novels",
        "fictional",
    )
    LANGUAGE_CHOICES = (
      'arabic',
      'english',
      'french',
    )
    P_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.URlField(max_length=200)
    Auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    isActive = models.BooleanField()
    is_rare = models.BooleanField()
    category = models.CharField(choices=CATEGORY_CHOICES)
    language = models.CharField(choices=LANGUAGE_CHOICES)


class Address(models.Model):
    ADDRESS_CHOICES =(
        'work',
        'home',
        'other'
    )
    A_id = models.AutoField(primary_key=True)
    address_type = models.CharField(choices=ADDRESS_CHOICES)
    address = models.CharField(max_length=30)


class Custumer(models.Model):
    C_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    add_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    gender = models.BooleanField()

class Branch(models.Model):
    B_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=30)
    address = models.ForeginKey(Address, on_delete=models.CASCADE)
    phone = models.FloatField();


class item(models.Model):
    it_id = models.AutoField(primary_key=True)
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    C_id = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    item_qty = models.IntegerField()

class Employee(models.Model):
    E_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    salary = models.FloatField()
    is_admin = models.BooleanField()
    B_id = models.ForeignKey(Branch, on_delete=models.CASCADE)


class order(models.Model):
    TEXT_CHOICES=(
        'internal',
        'external'
    )
    O_id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(item)
    total = models.FloatField()
    price = models.FloatField()
    C_id = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    E_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Delivery_type = models.CharField(choices=TEXT_CHOICES)

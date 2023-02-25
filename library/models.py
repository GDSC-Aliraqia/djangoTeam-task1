from django.db import models

# Create your models here.
class Address(models.Model):
    address_type = models.Choices()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    add_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    gender = models.BooleanField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.FloatField()

    def __str__(self):
        return self.branch_name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.FloatField()
    is_admin = models.BooleanField()
    B_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.CharField(max_length=100)
    total = models.FloatField()
    price = models.FloatField()
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    E_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Delivery_type = models.Choices()

    def __str__(self):
        return self.items


class Section(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Auth(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.URLField()
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    is_rare = models.BooleanField()
    category = models.Choices()
    language = models.Choices()

    def __str__(self):
        return self.name


class item(models.Model):
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_qty = models.IntegerField()

    def __str__(self):
        return self.item_qty


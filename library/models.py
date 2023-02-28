from django.db import models

# Create your models here.
class Address(models.Model):
    add_choices = (
        ("w","work"),
        ("h","home"),
        ("o","other")
    )
    address_type = models.Choices(choices=add_choices)
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
    order_choices = (
        ("i","intemal"),
        ("e","extemal"),
    )
    items = models.CharField(max_length=100)
    total = models.FloatField()
    price = models.FloatField()
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    E_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Delivery_type = models.Choices(choices = order_choices)

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
    choices_category = (
        ("s","scientific"),
        ("a", "art"),
        ("h", "historic"),
        ("n", "novels"),
        ("f", "fictional)"
        )
    choices_language = (
        
        ("a","arabic"),
        ("e","english"),
        ("f","french")
    )
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.URLField()
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    is_rare = models.BooleanField()
    category = models.Choices(choices = choices_category)
    language = models.Choices(choices = choices_language)

    def __str__(self):
        return self.name


class item(models.Model):
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_qty = models.IntegerField()

    def __str__(self):
        return self.item_qty


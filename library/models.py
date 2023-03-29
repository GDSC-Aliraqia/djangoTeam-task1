from django.db import models
class section(models.Model):
    name = models.CharField( max_length=50)
    is_active = models.BooleanField()
    
class auth(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    category_choices = [
        ('S', 'Science'),
        ('A', 'Art'),
        ('H', 'Historic'),
        ('N', 'Novels'),
        ('F', 'Fictional'),
    ]
    Language_choices = [
        ('E', 'English'),
        ('A', 'Arabic'),
        ('F', 'French'),
    ]
    name = models.CharField( max_length=50)
    section = models.ForeignKey(section, on_delete=models.CASCADE)
    price = models.DecimalField( max_digits=5, decimal_places=2)
    image = models.URLField(max_length=200)
    auth = models.ForeignKey(auth, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    is_rare = models.BooleanField()
    category = models.CharField(max_length=50, choices=category_choices)
    language = models.CharField(max_length=50, choices=Language_choices)

class Address(models.Model):
    add_choices = (
        ("w","work"),
        ("h","home"),
        ("o","other")
    )
    address_type = models.Choices(choices=add_choices, max_length=100)
    address = models.CharField(max_length=100)

class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.FloatField()

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.FloatField()
    is_admin = models.BooleanField()
    B_id = models.ForeignKey(Branch, on_delete=models.CASCADE)

class customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    add_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    gender = models.BooleanField()

class order(models.Model):
    delivery_choices = [
        ('i', 'internal')
        ('e','external')
    ]
    items = models.ManyToManyField()
    total = models.FloatField() 
    price = models.FloatField()
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    branch =  models.ForeignKey(Branch, on_delete=models.CASCADE)
    employee =  models.ForeignKey(Employee, on_delete=models.CASCADE)
    deliverytype = models.CharField( max_length=50, choices=delivery_choices)   

class item(models.Model):
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    C_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    item_qty = models.IntegerField()







# Create your models here.

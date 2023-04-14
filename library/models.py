from django.db import models


<<<<<<< HEAD
# Create your models here.

class Section(models.TextChoices):
    BookStore = 'Book_Store', 'Book_Store'
    DrawSore = 'Draw_Store', 'Draw_Store'


class Product(models.Model):
    name = models.CharField(verbose_name='product_name', max_length=255)
    section = models.CharField('section', max_length=100, choices=Section.choices)
    price = models.FloatField(verbose_name='product_price', default=0.0)
    image = models.URLField('product_image', blank=True, null=True)

    # choices Data Field
    # The first element in each tuple is the actual value to be set on the model, 
    # and the second element is the human-readable name. For example:
    language = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('AR', 'Arabic'),
        ('EN', 'English'),
        ('FR', 'Franch'),
    ]),
    category = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Scientific', 'Scientific'),
        ('Art', 'Art'),
        ('Historic', 'Historic'),
        ('Novels', 'Novels'),
        ('Fictional', 'Fictional'),
    ])

    # Here is Boolean Field 
    # A true/false field.
    is_active = models.BooleanField('is_active', default=True)
    is_rare = models.BooleanField('is_rare', default=False)
    is_DrawTool = models.BooleanField('is_book', default=False)
    auth = models.ForeignKey('BookAuth', null=True, blank=True, on_delete=models.SET_NULL)


class BookAuth(models.Model):
    name = models.CharField('auth_name', max_length=100)
    email = models.EmailField('auth_email', max_length=254, null=True, blank=True)
    phone = models.CharField('auth_phone', max_length=100)
    number_of_book = models.IntegerField('number_of_book', default=0)
=======
class BookAuth(models.Model):
    A_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    
class Address(models.Model):
    A_id = models.BigAutoField(primary_key=True)
    address_type = [
    ('wo', 'Work'),
    ('ho', 'Home'),
    ('ot', 'Other')
    ]
    Address_type = models.CharField(max_length=2, choices=address_type)
    address = models.CharField(max_length=100)
      
      
class Section(models.Model):
    Ca_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_active=models.BooleanField()   
    
    
class Product(models.Model):
    P_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.URLField(max_length=100)
    auth = models.ForeignKey(BookAuth, on_delete=models.CASCADE)
    is_active=models.BooleanField()
    is_rare=models.BooleanField()
    category = [
        ('Sc', 'scientific'),
        ('Ar', 'art'),
        ('Hi', 'historic'),
        ('No', 'novels'),
        ('Fi', 'fictional')
    ]
    language = [
        ('ar', 'Arabic'),
        ('en', 'English'),
        ('fr', 'French')
    ]
    Category = models.CharField(max_length=2, choices=category)
    Language = models.CharField(max_length=2, choices=language)
    
    
class Customer(models.Model):
    C_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Add_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    gender=models.FloatField()
   
   
class Item(models.Model): 
    It_id = models.BigAutoField(primary_key=True)
    P_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    C_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item_qty=models.IntegerField()
    
    
class Branch(models.Model):
    
    B_id = models.BigAutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.FloatField()    


class Employee(models.Model):
    E_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    postion = models.CharField(max_length=100)
    salary = models.FloatField()
    is_admin=models.BooleanField()
    B_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
           
           
class Order(models.Model):
    O_id = models.BigAutoField(primary_key=True)
    items =  models.ManyToManyField(Item)
    total = models.FloatField(max_length=100)
    price=models.FloatField()
    C_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    E_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    delivery_type = [
        ('ch', 'Choices'),
        ('in', 'Internal'),
        ('ex', 'Exterbal')
    ]
    Delivery_type = models.CharField(max_length=2, choices=delivery_type)
>>>>>>> 14fce27 (mytask)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerDetail(models.Model):
    STATE_CHOICES = [
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli and Daman and Diu'),
        ('DL', 'Delhi'),
        ('JK', 'Jammu and Kashmir'),
        ('LA', 'Ladakh'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # we have created Many-to-one relationship i.e multiple order can be done by one user
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.IntegerField(
        default=0,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return str(self.id)
    
class Mens(models.Model):

    CATEGORY_CHOICES = [
        ('SUITS', 'Suits'),
        ('SHIRTS', 'Shirts'),
        ('WEDDING SHERWANI', 'Wedding Sherwani'),
        
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    small_description=models.CharField(max_length=300)
    description=models.TextField()
    selling_price = models.IntegerField()
    discounted_price = models.IntegerField()
    percentage = models.IntegerField(default=0)
    price_and_quantity_total = models.IntegerField(default=0)
    mens_image =models.ImageField(upload_to='mens_images')  # As we are using image field we have to intall 'pillow'. And we have to Define MEDIA_URL in settings.py file so that all folder should save in media directory

    def __str__(self):
        return str(self.id)
    

             # Quantity cannot be negative so we have used PositiveIntegerField

    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Mens, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=3, choices=[
        ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')
    ])

    def __str__(self):
        return str(self.id)
    
 


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mens = models.ForeignKey(Mens, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    customer = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return str(self.id)
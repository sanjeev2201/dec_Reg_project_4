from django.db import models
#'username','email','password','contact_no'
# Create your models here.
class Customer(models.Model):
    Customer_Id = models.IntegerField(primary_key=True)
    Customer_name = models.CharField(max_length=100)
    email_Id = models.EmailField()
    password = models.CharField(max_length=100) 
    conf_pass = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=15)

    class Meta:
        ordering = ["Customer_Id"]
        db_table = 'Customer'


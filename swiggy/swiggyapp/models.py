from django.db import models
from django.contrib import admin
class OrderTransaction(models.Model):
    Order_id = models.IntegerField(primary_key=True)
    User_id = models.IntegerField()
    Order_date = models.DateTimeField(auto_now_add=True)
    Item_name = models.CharField(max_length=200)
    Order_qty = models.IntegerField()
    Unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    Total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    Delivery_address = models.CharField(max_length=300)
    
class OrderTransactionAdmin(admin.ModelAdmin):
    list_display=('Order_id','User_id','Order_date','Item_name','Order_qty','Unit_price','Total_amount','Delivery_address')
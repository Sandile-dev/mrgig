from django.db import models
from twilio.rest import Client 


class Customer(models.Model):
    TYPES = (
        ('SMS','SMS'),
        ('WhatsApp','WhatsApp'),
        ('Email','Email')
    )

    sender_name = models.CharField(max_length=200, null=True)
    sender_surname = models.CharField(max_length=200, null=True)
    sender_phone = models.CharField(max_length=10, null=True)
    receiver_name = models.CharField(max_length=200, null=True)
    receiver_surname = models.CharField(max_length=200, null=True)
    receiver_phone = models.CharField(max_length=10, null=True)
    notification = models.CharField(max_length=200, null=True, choices=TYPES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s %s" % (self.sender_name, self.sender_surname)


class Parcel(models.Model):
    STATUS = (
        ('New', 'New'),
        ('On the Route', 'On the Route'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    refNumber = models.CharField(max_length=200, null=True)
    origination = models.CharField(max_length=200, null=True)
    destination = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.refNumber


class DriverRoute(models.Model):
    TYPES = (
        ('Eastern Cape','Eastern Cape'),
        ('Free State','Free State'),
        ('Gauteng','Gauteng'),
        ('KwaZulu-Natal','KwaZulu-Natal'),
        ('Limpopo','Limpopo'),
        ('Mpumalanga','Mpumalanga'),
        ('Northern Cape','Northern Cape'),
        ('North West','North West'),
        ('Western Cape','Western Cape'),
    )
    
    province = models.CharField(max_length=200, null=True, choices=TYPES)
    city = models.CharField(max_length=200, null=True)
    town = models.CharField(max_length=200, null=True)
    rankName = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rankName


class Partner(models.Model):
    parcel = models.ForeignKey(Parcel,on_delete=models.CASCADE, null=True)
    driver_route = models.ForeignKey(DriverRoute, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(max_length=200, null=True)
    taxiRegNumber = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.name 
   
    def save(self, *args, **kwargs):
        if self.parcel.status == 'On the Route' or self.parcel.status == 'Out for Delivery':
            account_sid = 'ACa547faabb72f7ffe07d09e204e208c21' 
            auth_token = '0a897ada1583e0fb8be092fd8dd01c06' 
            client = Client(account_sid, auth_token) 

            message = client.messages.create(  
                                messaging_service_sid='MGce9b46db7c19792ccc21784134db1d26', 
                                body= f" Dear {self.parcel.customer.sender_name} {self.parcel.customer.sender_surname}, please be advised your parcel with reference number {self.parcel.refNumber} is {self.parcel.status} to {self.parcel.destination}. You may track your parcel on the following link: https://taxicourier.co.za/",      
                                to=f"{self.parcel.customer.sender_phone.replace('0','+27',1)}"
                            )
            receiver_message = client.messages.create(  
                                messaging_service_sid='MGce9b46db7c19792ccc21784134db1d26', 
                                body= f" Dear {self.parcel.customer.receiver_name} {self.parcel.customer.receiver_surname}, please be advised your parcel with reference number {self.parcel.refNumber} is {self.parcel.status} to {self.parcel.destination}. You may track your parcel on the following link: https://taxicourier.co.za/",      
                                to=f"{self.parcel.customer.receiver_phone.replace('0','+27',1)}"
                            )
        else: 
            account_sid = 'ACa547faabb72f7ffe07d09e204e208c21' 
            auth_token = '0a897ada1583e0fb8be092fd8dd01c06' 
            client = Client(account_sid, auth_token) 

            message = client.messages.create(  
                                messaging_service_sid='MGce9b46db7c19792ccc21784134db1d26', 
                                body= f" Dear {self.parcel.customer.sender_name} {self.parcel.customer.sender_surname}, please be advised your parcel with reference number {self.parcel.refNumber} has been {self.parcel.status} to {self.parcel.destination}. You may track your parcel on the following link: https://taxicourier.co.za/",      
                                to=f"{self.parcel.customer.sender_phone.replace('0','+27',1)}"
                            )
            receiver_message = client.messages.create(  
                                messaging_service_sid='MGce9b46db7c19792ccc21784134db1d26', 
                                body= f" Dear {self.parcel.customer.receiver_name} {self.parcel.customer.receiver_surname}, please be advised your parcel with reference number {self.parcel.refNumber} is {self.parcel.status} to {self.parcel.destination}. You may track your parcel on the following link: https://taxicourier.co.za/",      
                                to=f"{self.parcel.customer.receiver_phone.replace('0','+27',1)}"
                            )

            print(message.sid, receiver_message.sid) 
        return super().save(*args, **kwargs)
   

    


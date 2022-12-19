# Generated by Django 4.1 on 2022-12-03 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=200, null=True)),
                ('sender_surname', models.CharField(max_length=200, null=True)),
                ('sender_phone', models.CharField(max_length=10, null=True)),
                ('receiver_name', models.CharField(max_length=200, null=True)),
                ('receiver_surname', models.CharField(max_length=200, null=True)),
                ('receiver_phone', models.CharField(max_length=10, null=True)),
                ('notification', models.CharField(choices=[('SMS', 'SMS'), ('WhatsApp', 'WhatsApp'), ('Email', 'Email')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DriverRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('Eastern Cape', 'Eastern Cape'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng'), ('KwaZulu-Natal', 'KwaZulu-Natal'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ('Northern Cape', 'Northern Cape'), ('North West', 'North West'), ('Western Cape', 'Western Cape')], max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('town', models.CharField(max_length=200, null=True)),
                ('rankName', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refNumber', models.CharField(max_length=200, null=True)),
                ('origination', models.CharField(max_length=200, null=True)),
                ('destination', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('On the Route', 'On the Route'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Closed', 'Closed')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('surname', models.CharField(max_length=200, null=True)),
                ('phoneNumber', models.CharField(max_length=200, null=True)),
                ('taxiRegNumber', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('driver_route', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.driverroute')),
                ('parcel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.parcel')),
            ],
        ),
    ]
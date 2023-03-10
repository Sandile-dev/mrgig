# Generated by Django 4.1 on 2022-12-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcel',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='parcel',
        ),
        migrations.AlterField(
            model_name='parcel',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('On the Route', 'On the Route'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Returned', 'Returned'), ('Closed', 'Closed')], max_length=200, null=True),
        ),
    ]

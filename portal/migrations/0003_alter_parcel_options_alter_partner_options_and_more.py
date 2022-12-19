# Generated by Django 4.1 on 2022-12-11 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_remove_parcel_customer_remove_partner_parcel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parcel',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={'ordering': ['date_created']},
        ),
        migrations.AddField(
            model_name='parcel',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.customer'),
        ),
        migrations.AddField(
            model_name='partner',
            name='parcel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.parcel'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='driver_route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.driverroute'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-08-20 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='adddress',
            new_name='address',
        ),
    ]

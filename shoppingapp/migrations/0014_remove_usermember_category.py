# Generated by Django 4.1.7 on 2023-04-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shoppingapp", "0013_remove_usermember_image_product_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="usermember", name="category",),
    ]

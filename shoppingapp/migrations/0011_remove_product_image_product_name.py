# Generated by Django 4.1.7 on 2023-04-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shoppingapp", "0010_remove_product_name"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="image",),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(default="default value", max_length=255),
        ),
    ]

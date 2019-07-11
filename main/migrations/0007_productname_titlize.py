# Generated by Django 2.2.3 on 2019-07-11 23:35

from django.db import migrations


class Migration(migrations.Migration):

    def make_title(apps, schema):
        Product = apps.get_model('main','Product')
        for product in Product.objects.all():
            product.name = product.name.title()
            product.save()

    dependencies = [
        ('main', '0006_productname_capitalize'),
    ]

    operations = [
        migrations.RunPython(
            make_title,
            migrations.RunPython.noop
        )
    ]

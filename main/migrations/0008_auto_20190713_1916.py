# Generated by Django 2.2.3 on 2019-07-13 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productname_titlize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttag',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='main.ProductTag'),
        ),
    ]
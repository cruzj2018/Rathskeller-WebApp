# Generated by Django 3.2 on 2021-04-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rath', '0002_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

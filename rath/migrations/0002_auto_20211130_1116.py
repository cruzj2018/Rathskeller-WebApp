# Generated by Django 3.2.9 on 2021-11-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rath', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-created',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-created',), 'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': 'Food Section'},
        ),
    ]

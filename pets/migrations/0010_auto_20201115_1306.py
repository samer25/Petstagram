# Generated by Django 3.1.2 on 2020-11-15 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0009_auto_20201115_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='image',
            new_name='images',
        ),
    ]
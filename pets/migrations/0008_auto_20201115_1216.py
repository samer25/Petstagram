# Generated by Django 3.1.2 on 2020-11-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image_url',
            field=models.FileField(upload_to=''),
        ),
    ]

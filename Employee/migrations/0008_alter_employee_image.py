# Generated by Django 3.2.3 on 2021-06-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_auto_20210603_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(upload_to='employee_pictures'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0010_alter_employee_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]

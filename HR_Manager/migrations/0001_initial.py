# Generated by Django 3.2.3 on 2021-06-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('name', models.TextField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('cnic', models.TextField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
    ]
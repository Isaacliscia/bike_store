# Generated by Django 2.1.3 on 2018-11-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=264, unique=True),
        ),
    ]

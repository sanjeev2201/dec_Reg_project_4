# Generated by Django 4.1 on 2022-12-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reg_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Contact_no',
            field=models.CharField(max_length=15),
        ),
    ]

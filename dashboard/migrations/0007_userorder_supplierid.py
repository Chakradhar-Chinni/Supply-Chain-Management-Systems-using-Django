# Generated by Django 3.1.7 on 2021-06-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210621_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='SupplierId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

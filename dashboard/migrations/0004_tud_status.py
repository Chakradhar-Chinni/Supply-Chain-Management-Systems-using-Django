# Generated by Django 3.1.7 on 2021-06-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_tmd_tud'),
    ]

    operations = [
        migrations.AddField(
            model_name='tud',
            name='Status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

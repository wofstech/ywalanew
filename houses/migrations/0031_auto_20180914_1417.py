# Generated by Django 2.0.1 on 2018-09-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0030_auto_20180914_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='myhouses',
            name='Account_name',
            field=models.CharField(default='ss', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myhouses',
            name='Account_number',
            field=models.IntegerField(default=66),
            preserve_default=False,
        ),
    ]

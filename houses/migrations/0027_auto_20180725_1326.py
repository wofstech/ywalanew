# Generated by Django 2.0.1 on 2018-07-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0026_myhouses_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myhouses',
            name='Payment_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

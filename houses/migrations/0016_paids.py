# Generated by Django 2.0.1 on 2018-07-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0015_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('myRef', models.CharField(max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-06-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_profile_if_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='if_student',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
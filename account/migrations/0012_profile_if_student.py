# Generated by Django 2.0.1 on 2018-06-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_profile_type_of_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='if_student',
            field=models.CharField(default='ful', max_length=200),
            preserve_default=False,
        ),
    ]

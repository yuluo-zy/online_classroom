# Generated by Django 2.0.5 on 2018-05-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=105, verbose_name='地址'),
        ),
    ]

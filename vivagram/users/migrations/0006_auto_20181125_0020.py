# Generated by Django 2.0.9 on 2018-11-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181125_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not specified'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_userservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userservice',
            name='identity',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

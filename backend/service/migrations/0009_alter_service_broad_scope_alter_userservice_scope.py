# Generated by Django 4.1.3 on 2022-12-12 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_rename_user_refresh_taken_userservice_user_refresh_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='broad_scope',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userservice',
            name='scope',
            field=models.TextField(default='read', null=True),
        ),
    ]

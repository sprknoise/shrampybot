# Generated by Django 4.1.3 on 2022-12-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_service_broad_scope_alter_userservice_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='streaming_service',
            field=models.BooleanField(default=True),
        ),
    ]

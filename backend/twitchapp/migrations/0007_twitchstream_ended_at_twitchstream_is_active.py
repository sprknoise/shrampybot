# Generated by Django 4.1.3 on 2022-12-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitchapp', '0006_twitchcategory_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchstream',
            name='ended_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='twitchstream',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

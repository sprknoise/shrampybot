# Generated by Django 4.1.3 on 2022-12-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitchapp', '0003_alter_twitchcategory_twitch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]

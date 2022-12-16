# Generated by Django 4.1.3 on 2022-12-15 00:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_alter_stream_platform_delete_streamingplatform'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='guid',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]

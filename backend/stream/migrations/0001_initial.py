# Generated by Django 4.1.3 on 2022-12-13 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0009_alter_service_broad_scope_alter_userservice_scope'),
        ('streamer', '0015_alter_streamer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden', models.BooleanField(default=False)),
                ('streamer', models.ManyToManyField(to='streamer.streamer')),
            ],
        ),
        migrations.CreateModel(
            name='StreamingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('api_info', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='service.service')),
            ],
        ),
        migrations.CreateModel(
            name='StreamAssoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_stream_id', models.CharField(max_length=255)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='stream.streamingplatform')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='stream.stream')),
            ],
        ),
        migrations.AddConstraint(
            model_name='streamassoc',
            constraint=models.UniqueConstraint(fields=('platform', 'stream', 'platform_stream_id'), name='unique stream_assoc'),
        ),
    ]

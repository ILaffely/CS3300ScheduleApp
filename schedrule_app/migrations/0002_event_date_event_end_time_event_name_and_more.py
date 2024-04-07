# Generated by Django 4.2 on 2024-04-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedrule_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=None),
        ),
    ]

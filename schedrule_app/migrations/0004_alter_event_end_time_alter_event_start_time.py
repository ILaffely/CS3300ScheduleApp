# Generated by Django 4.2 on 2024-04-07 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedrule_app', '0003_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
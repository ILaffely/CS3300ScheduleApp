# Generated by Django 4.2 on 2024-04-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedrule_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='end_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

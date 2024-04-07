# Generated by Django 4.2 on 2024-04-07 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(blank=True, choices=[('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow')], max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schedrule_app.eventtype')),
            ],
        ),
    ]

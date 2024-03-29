# Generated by Django 3.1 on 2020-08-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0003_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='Featured',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Featured_Price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Price_hour',
        ),
        migrations.RemoveField(
            model_name='service',
            name='Price_service',
        ),
        migrations.AddField(
            model_name='main',
            name='Bio',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='Instrument',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main',
            name='Organization',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='Description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

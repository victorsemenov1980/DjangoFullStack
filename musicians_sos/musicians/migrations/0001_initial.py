# Generated by Django 3.1 on 2020-08-08 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Questions', models.TextField()),
                ('Answers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('Service_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=255)),
                ('Sub_Category', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price_hour', models.FloatField(blank=True, default=0.0)),
                ('Price_service', models.FloatField(blank=True, default=0.0)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=255)),
                ('CoverLetter', models.TextField()),
                ('Photo', models.ImageField(upload_to='images/')),
                ('Icon', models.ImageField(upload_to='images/')),
                ('IsValid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Featured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Price', models.FloatField(default=0.0)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

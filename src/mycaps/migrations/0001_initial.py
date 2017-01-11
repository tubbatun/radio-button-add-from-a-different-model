# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-10 10:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True, verbose_name='updated on')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='colors/%Y/%m/%d', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True, verbose_name='updated on')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, unique=True, verbose_name='slug')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now=True, null=True, verbose_name='updated on')),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packagebycoffee', to='mycaps.Coffee', verbose_name='coffee')),
                ('color', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='packagebycolor', to='mycaps.Color', verbose_name='color')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'package',
                'verbose_name_plural': 'packages',
            },
        ),
    ]

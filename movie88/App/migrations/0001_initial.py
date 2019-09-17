# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-09-16 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=60)),
                ('parentid', models.IntegerField()),
                ('orderby', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
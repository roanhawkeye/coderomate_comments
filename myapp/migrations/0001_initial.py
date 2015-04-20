# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('created_data', models.DateTimeField(auto_now_add=True)),
                ('last_updated_data', models.DateTimeField(auto_now=True)),
                ('is_inappropriate', models.BooleanField()),
                ('ranking', models.IntegerField(default=1, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
            ],
        ),
    ]

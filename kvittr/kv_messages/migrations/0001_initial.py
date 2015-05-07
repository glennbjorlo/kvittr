# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=15)),
                ('umessage', models.CharField(max_length=140)),
                ('thumbs_up', models.PositiveIntegerField(default=0)),
                ('created_datetime', models.DateTimeField()),
            ],
        ),
    ]

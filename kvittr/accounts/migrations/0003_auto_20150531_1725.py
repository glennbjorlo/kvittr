# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150531_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatepicture',
            name='user_picture',
            field=models.ImageField(upload_to=b'media/theme/user_images/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatepicture',
            name='user_picture',
            field=models.ImageField(default=b'static/theme/images/675432109.jpg', upload_to=b'static/theme/user_images/'),
        ),
    ]

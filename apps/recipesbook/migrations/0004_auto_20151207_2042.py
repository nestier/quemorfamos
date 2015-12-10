# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesbook', '0003_auto_20151207_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='datetime',
            field=models.DateTimeField(verbose_name=b'date_published'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='datetime',
            field=models.DateTimeField(verbose_name=b'date_published'),
        ),
    ]

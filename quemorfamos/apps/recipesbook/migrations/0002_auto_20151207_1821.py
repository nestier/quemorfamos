# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='ingredient',
            field=models.ForeignKey(default=1, to='recipesbook.Ingredient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amount',
            name='recipe',
            field=models.ForeignKey(default=1, to='recipesbook.Recipe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipesbook.Ingredient', through='recipesbook.Amount'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180823_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章正文'),
        ),
    ]

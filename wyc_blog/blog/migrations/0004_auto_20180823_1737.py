# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogspost_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='body',
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='timestamp',
            field=models.DateTimeField(verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='title',
            field=models.CharField(verbose_name='文章标题', max_length=150),
        ),
    ]

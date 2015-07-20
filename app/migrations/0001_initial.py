# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_tel', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_info', models.TextField()),
                ('learn_classification', models.CharField(max_length=50)),
                ('learn_per_day', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='UserLearn',
            fields=[
                ('learn_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=11)),
                ('word_id', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='UserWordsComment',
            fields=[
                ('comment_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField(verbose_name=11)),
                ('word_id', models.IntegerField(verbose_name=11)),
                ('comments', models.TextField()),
                ('if_open', models.IntegerField(verbose_name=1)),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('word_id', models.AutoField(serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=50)),
                ('word_explanation_ch', models.CharField(max_length=400)),
                ('word_explanation_en', models.CharField(max_length=400)),
                ('example_sentence', models.CharField(max_length=400)),
                ('word_classification', models.CharField(max_length=50)),
            ],
        ),
    ]

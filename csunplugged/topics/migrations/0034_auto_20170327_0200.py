# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0033_curriculumarea_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculumarea',
            name='parent',
        ),
        migrations.AddField(
            model_name='curriculumarea',
            name='parent',
            field=models.ManyToManyField(related_name='_curriculumarea_parent_+', to='topics.CurriculumArea'),
        ),
    ]

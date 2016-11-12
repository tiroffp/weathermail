# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('email', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='city',
            field=models.ForeignKey(to='signup.City'),
        ),
    ]

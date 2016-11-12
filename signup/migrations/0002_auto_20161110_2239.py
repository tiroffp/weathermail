# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attendee',
            new_name='Subscriber',
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.TextField(default='MA'),
            preserve_default=False,
        ),
    ]

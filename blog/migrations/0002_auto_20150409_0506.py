# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='posts',
            name='owner',
        ),
        migrations.AddField(
            model_name='posts',
            name='body',
            field=models.TextField(default=datetime.datetime(2015, 4, 9, 5, 6, 50, 384285, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 9, 5, 6, 57, 784309, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]

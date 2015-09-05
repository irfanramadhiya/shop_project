# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categories', models.CharField(max_length=200, choices=[(b'B', b'Bed Sheet'), (b'T', b'Table Cloth'), (b'N', b'Napkins'), (b'C', b'Cushion Cover')])),
                ('name', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200, choices=[(b'SK', b'Super King Size'), (b'K', b'King Size'), (b'Q', b'Queen Size'), (b'S', b'Single Size'), (b'6', b'For 6 Person'), (b'8', b'For 8 Person'), (b'10', b'For 10 Person'), (b'12', b'For 12 Person')])),
                ('color', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('material', models.CharField(max_length=200)),
                ('is_available', models.BooleanField(default=True)),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

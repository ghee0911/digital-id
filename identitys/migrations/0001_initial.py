# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-04 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iddata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('idnumber', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('finger', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Inputdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint', models.ImageField(upload_to='')),
                ('input_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selection_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='inputdata',
            name='selection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identitys.Selection'),
        ),
        migrations.AddField(
            model_name='iddata',
            name='inputdata',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identitys.Inputdata'),
        ),
    ]

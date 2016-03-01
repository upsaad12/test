# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30)),
                ('Prenom', models.CharField(max_length=30)),
                ('Nom_de_compte', models.CharField(max_length=30)),
                ('mot_de_passe', models.CharField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30)),
                ('Prenom', models.CharField(max_length=30)),
                ('Adresse', models.CharField(max_length=100)),
                ('Nom_de_compte', models.CharField(max_length=30)),
                ('mot_de_passe', models.CharField(max_length=42)),
            ],
        ),
        migrations.AddField(
            model_name='enfant',
            name='parent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='basededonnee.Parent'),
        ),
    ]

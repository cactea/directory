# Generated by Django 2.0.5 on 2018-09-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CACTEA', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cactea',
            options={'ordering': ['id'], 'verbose_name': 'cactea', 'verbose_name_plural': 'cacteas'},
        ),
    ]

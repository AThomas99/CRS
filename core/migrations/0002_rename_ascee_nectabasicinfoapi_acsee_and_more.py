# Generated by Django 4.0.4 on 2022-04-26 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nectabasicinfoapi',
            old_name='ASCEE',
            new_name='acsee',
        ),
        migrations.RenameField(
            model_name='nectabasicinfoapi',
            old_name='CSEE',
            new_name='csee',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ASCEE',
            new_name='acsee',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='CSEE',
            new_name='csee',
        ),
    ]
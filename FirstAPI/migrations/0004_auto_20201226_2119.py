# Generated by Django 3.1.4 on 2020-12-26 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FirstAPI', '0003_auto_20201224_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='posts',
            new_name='tags',
        ),
    ]
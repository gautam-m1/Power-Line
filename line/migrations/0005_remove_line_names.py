# Generated by Django 4.0.5 on 2022-06-26 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0004_alter_line_wear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='names',
        ),
    ]

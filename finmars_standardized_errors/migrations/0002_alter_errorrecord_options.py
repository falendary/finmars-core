# Generated by Django 4.1.3 on 2022-12-15 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finmars_standardized_errors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errorrecord',
            options={'ordering': ['-created']},
        ),
    ]

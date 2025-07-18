# Generated by Django 4.1.3 on 2023-06-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_tasks', '0006_alter_celerytask_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='celerytask',
            name='expiry_at',
            field=models.DateTimeField(blank=True, db_index=True, help_text='Autogenerated. Task will be canceled after this time.', null=True, verbose_name='expiry at'),
        ),
        migrations.AddField(
            model_name='celerytask',
            name='ttl',
            field=models.PositiveIntegerField(default=0, help_text='Amount of time to complet task before automatic cancelation. 0 - no limit.', verbose_name='time to live'),
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-12 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('celery_tasks', '0003_initial'),
        ('procedures', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdatafileprocedureinstance',
            name='linked_import_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='celery_tasks.celerytask', verbose_name='linked import task'),
        ),
    ]

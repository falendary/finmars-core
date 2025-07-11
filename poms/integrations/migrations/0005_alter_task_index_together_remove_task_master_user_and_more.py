# Generated by Django 4.1.3 on 2023-03-21 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0004_complextransactionimportschemerulescenario_status'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='task',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='task',
            name='master_user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='member',
        ),
        migrations.RemoveField(
            model_name='task',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='task',
            name='provider',
        ),
        migrations.DeleteModel(
            name='PricingAutomatedSchedule',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

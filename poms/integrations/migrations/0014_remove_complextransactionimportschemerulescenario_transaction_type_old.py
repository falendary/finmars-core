# Generated by Django 4.1.3 on 2023-05-12 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0013_complextransactionimportschemerulescenario_transaction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complextransactionimportschemerulescenario',
            name='transaction_type_old',
        ),
    ]

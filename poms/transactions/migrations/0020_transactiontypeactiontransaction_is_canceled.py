# Generated by Django 4.1.3 on 2023-04-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transactions", "0019_alter_transaction_user_number_1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactiontypeactiontransaction",
            name="is_canceled",
            field=models.CharField(
                blank=True, max_length=4096, null=True, verbose_name="is canceled"
            ),
        ),
    ]

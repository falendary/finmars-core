# Generated by Django 4.2.3 on 2024-03-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_member_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masteruser",
            name="base_api_url",
            field=models.CharField(
                default="space00000",
                max_length=255,
                unique=True,
                verbose_name="base api url",
            ),
            preserve_default=False,
        ),
    ]

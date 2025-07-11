# Generated by Django 4.2.8 on 2024-04-11 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_tokens", "0003_personalaccesstoken"),
    ]

    operations = [
        migrations.AddField(
            model_name="personalaccesstoken",
            name="access_level",
            field=models.CharField(
                choices=[
                    ("read", "Read Only"),
                    ("write", "Write Access"),
                    ("admin", "Admin Access"),
                ],
                default="read",
                max_length=10,
            ),
        ),
    ]

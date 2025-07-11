# Generated by Django 4.1.3 on 2022-12-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_code",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="user code"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "short_name",
                    models.TextField(blank=True, null=True, verbose_name="short name"),
                ),
                (
                    "public_name",
                    models.CharField(
                        blank=True,
                        help_text="used if user does not have permissions to view object",
                        max_length=255,
                        null=True,
                        verbose_name="public name",
                    ),
                ),
                (
                    "notes",
                    models.TextField(blank=True, null=True, verbose_name="notes"),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="is enabled"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        null=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="modified"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="is deleted"
                    ),
                ),
                (
                    "deleted_user_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="deleted user code",
                    ),
                ),
                (
                    "is_valid_for_all_portfolios",
                    models.BooleanField(
                        default=True, verbose_name="is valid for all portfolios"
                    ),
                ),
            ],
            options={
                "verbose_name": "account",
                "verbose_name_plural": "accounts",
                "ordering": ["user_code"],
                "permissions": [("manage_account", "Can manage account")],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AccountType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_code",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="user code"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "short_name",
                    models.TextField(blank=True, null=True, verbose_name="short name"),
                ),
                (
                    "public_name",
                    models.CharField(
                        blank=True,
                        help_text="used if user does not have permissions to view object",
                        max_length=255,
                        null=True,
                        verbose_name="public name",
                    ),
                ),
                (
                    "notes",
                    models.TextField(blank=True, null=True, verbose_name="notes"),
                ),
                (
                    "is_enabled",
                    models.BooleanField(
                        db_index=True, default=True, verbose_name="is enabled"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        null=True,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="modified"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(
                        db_index=True, default=False, verbose_name="is deleted"
                    ),
                ),
                (
                    "deleted_user_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="deleted user code",
                    ),
                ),
                (
                    "show_transaction_details",
                    models.BooleanField(
                        default=False, verbose_name="show transaction details"
                    ),
                ),
                (
                    "transaction_details_expr",
                    models.CharField(
                        blank=True,
                        max_length=4096,
                        null=True,
                        verbose_name="transaction details expr",
                    ),
                ),
            ],
            options={
                "verbose_name": "account type",
                "verbose_name_plural": "account types",
                "ordering": ["user_code"],
                "permissions": [("manage_accounttype", "Can manage account type")],
                "abstract": False,
            },
        ),
    ]

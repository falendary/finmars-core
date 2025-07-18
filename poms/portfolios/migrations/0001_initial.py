# Generated by Django 4.1.3 on 2022-12-07 21:41

from django.db import migrations, models
import django.db.models.deletion
import poms.common.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='user code')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('short_name', models.TextField(blank=True, null=True, verbose_name='short name')),
                ('public_name', models.CharField(blank=True, help_text='used if user does not have permissions to view object', max_length=255, null=True, verbose_name='public name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('is_enabled', models.BooleanField(db_index=True, default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='is deleted')),
                ('deleted_user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='deleted user code')),
            ],
            options={
                'verbose_name': 'portfolio',
                'verbose_name_plural': 'portfolios',
                'ordering': ['user_code'],
                'permissions': (('manage_portfolio', 'Can manage portfolio'),),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='user code')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('short_name', models.TextField(blank=True, null=True, verbose_name='short name')),
                ('public_name', models.CharField(blank=True, help_text='used if user does not have permissions to view object', max_length=255, null=True, verbose_name='public name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('is_enabled', models.BooleanField(db_index=True, default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='is deleted')),
                ('deleted_user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='deleted user code')),
            ],
            options={
                'verbose_name': 'portfolio bundle',
                'verbose_name_plural': 'portfolio bundles',
                'ordering': ['user_code'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='user code')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('short_name', models.TextField(blank=True, null=True, verbose_name='short name')),
                ('public_name', models.CharField(blank=True, help_text='used if user does not have permissions to view object', max_length=255, null=True, verbose_name='public name')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('is_enabled', models.BooleanField(db_index=True, default=True, verbose_name='is enabled')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='is deleted')),
                ('deleted_user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='deleted user code')),
                ('default_price', models.FloatField(default=1.0, verbose_name='default price')),
            ],
            options={
                'verbose_name': 'portfolio register',
                'verbose_name_plural': 'portfolio registers',
                'ordering': ['user_code'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PortfolioRegisterRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('transaction_code', models.IntegerField(default=0, verbose_name='transaction code')),
                ('transaction_date', models.DateField(db_index=True, default=poms.common.utils.date_now, verbose_name='transaction date')),
                ('cash_amount', models.FloatField(default=0.0, help_text='Cash amount', verbose_name='cash amount')),
                ('fx_rate', models.FloatField(default=0.0, verbose_name='fx rate')),
                ('cash_amount_valuation_currency', models.FloatField(default=0.0, help_text='Cash amount valuation currency', verbose_name='cash amount valuation currency')),
                ('nav_previous_day_valuation_currency', models.FloatField(default=0.0, verbose_name='nav previous day valuation currency')),
                ('n_shares_previous_day', models.FloatField(default=0.0, verbose_name='n shares previous day')),
                ('n_shares_added', models.FloatField(default=0.0, verbose_name='n shares added')),
                ('dealing_price_valuation_currency', models.FloatField(default=0.0, help_text='Dealing price valuation currency', verbose_name='dealing price valuation currency')),
                ('rolling_shares_of_the_day', models.FloatField(default=0.0, verbose_name='rolling shares  of the day')),
            ],
            options={
                'verbose_name': 'portfolio register record',
                'verbose_name_plural': 'portfolio registers record',
            },
        ),
    ]

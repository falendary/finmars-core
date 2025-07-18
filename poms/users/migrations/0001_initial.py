# Generated by Django 4.1.3 on 2022-12-07 21:41

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'User')], db_index=True, default=2, verbose_name='role')),
                ('permission_table_json_data', models.TextField(blank=True, null=True, verbose_name='json data')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MasterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('base_api_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='base api url')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Online'), (2, 'Offline'), (3, 'Backup')], default=1, verbose_name='status')),
                ('language', models.CharField(default='en', max_length=5, verbose_name='language')),
                ('timezone', models.CharField(default='UTC', max_length=20, verbose_name='timezone')),
                ('notification_business_days', models.IntegerField(default=0)),
                ('user_code_counters', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('token', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='token')),
                ('unique_id', models.UUIDField(blank=True, null=True))
            ],
            options={
                'verbose_name': 'master user',
                'verbose_name_plural': 'master users',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='en', max_length=5, verbose_name='language')),
                ('timezone', models.CharField(default='UTC', max_length=20, verbose_name='timezone')),
                ('two_factor_verification', models.BooleanField(default=False, verbose_name='two factor verification')),
                ('user_unique_id', models.UUIDField(blank=True, null=True)),
                ('active_master_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.masteruser', verbose_name='master user')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='UsercodePrefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=80, verbose_name='prefix')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('master_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.masteruser', verbose_name='master user')),
            ],
        ),
        migrations.CreateModel(
            name='ResetPasswordToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was this token generated')),
                ('key', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Key')),
                ('ip_address', models.GenericIPAddressField(default='127.0.0.1', verbose_name='The IP address of this session')),
                ('user_agent', models.CharField(default='', max_length=256, verbose_name='HTTP User Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_reset_tokens', to=settings.AUTH_USER_MODEL, verbose_name='The User which is associated to this password reset token')),
            ],
            options={
                'verbose_name': 'Password Reset Token',
                'verbose_name_plural': 'Password Reset Tokens',
            },
        ),
        migrations.CreateModel(
            name='OtpToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('secret', models.CharField(blank=True, default='', editable=False, max_length=16, verbose_name='secret')),
                ('is_active', models.BooleanField(default=False, verbose_name='is active')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='otp_tokens', to=settings.AUTH_USER_MODEL, verbose_name='OTP Token')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, verbose_name='is deleted')),
                ('deleted_user_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='deleted user code')),
                ('username', models.CharField(blank=True, default='', editable=False, max_length=255, verbose_name='username')),
                ('first_name', models.CharField(blank=True, default='', editable=False, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, default='', editable=False, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, default='', editable=False, max_length=254, verbose_name='email')),
                ('notification_level', models.PositiveSmallIntegerField(choices=[(1, 'Do not notify'), (2, 'Show & Email notifications'), (3, 'Email notifications'), (4, 'Show notifications')], db_index=True, default=4, verbose_name='notification level')),
                ('interface_level', models.PositiveSmallIntegerField(db_index=True, default=20, verbose_name='interface level')),
                ('join_date', models.DateTimeField(auto_now_add=True, verbose_name='join date')),
                ('is_owner', models.BooleanField(default=False, verbose_name='is owner')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
                ('json_data', models.TextField(blank=True, null=True, verbose_name='json data')),
                ('groups', models.ManyToManyField(blank=True, related_name='members', to='users.group', verbose_name='groups')),
                ('master_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='users.masteruser', verbose_name='master user')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
                'ordering': ['username'],
                'abstract': False,
                'unique_together': {('master_user', 'user')},
                'index_together': {('master_user', 'is_deleted')},
            },
        ),
        migrations.AddField(
            model_name='group',
            name='master_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='users.masteruser', verbose_name='master user'),
        ),

        migrations.CreateModel(
            name='InviteToMasterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Sent'), (1, 'Accepted'), (2, 'Declined')], default=0)),
                ('from_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites_to_users', to='users.member', verbose_name='from_member')),
                ('groups', models.ManyToManyField(blank=True, related_name='invites', to='users.group', verbose_name='groups')),
                ('master_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites_to_users', to='users.masteruser', verbose_name='master user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites_to_master_user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'invite to master user',
                'verbose_name_plural': 'invites to master user',
                'unique_together': {('user', 'master_user')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='group',
            unique_together={('master_user', 'name')},
        ),
        migrations.CreateModel(
            name='FakeSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='name')),
                ('value', models.PositiveIntegerField(default=0, verbose_name='value')),
                ('master_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fake_sequences', to='users.masteruser', verbose_name='master user')),
            ],
            options={
                'verbose_name': 'fake sequence',
                'verbose_name_plural': 'fake sequences',
                'ordering': ['name'],
                'unique_together': {('master_user', 'name')},
            },
        ),
    ]

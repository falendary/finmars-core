# Generated by Django 4.1.3 on 2023-05-05 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_alter_invitetomasteruser_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPolicyTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('policy', models.JSONField(blank=True, help_text='Access Policy JSON', null=True, verbose_name='Policy')),
                ('configuration_code', models.CharField(default='com.finmars.local', max_length=255, verbose_name='Configuration Code')),
            ],
            options={
                'verbose_name': 'Access Policy Template',
                'verbose_name_plural': 'Access Policy Templates',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('configuration_code', models.CharField(default='com.finmars.local', help_text='Indicates that entity is part of Configuration and can be imported/exported.', max_length=255, verbose_name='Configuration Code')),
                ('members', models.ManyToManyField(blank=True, related_name='iam_groups', to='users.member')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('configuration_code', models.CharField(default='com.finmars.local', help_text='Indicates that entity is part of Configuration and can be imported/exported.', max_length=255, verbose_name='Configuration Code')),
                ('members', models.ManyToManyField(blank=True, related_name='iam_roles', to='users.member')),
            ],
        ),
        migrations.CreateModel(
            name='RoleAccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('policy', models.JSONField(blank=True, help_text='Access Policy JSON', null=True, verbose_name='Policy')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_policies', to='iam.role', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'User Access Policy',
                'verbose_name_plural': 'User Access Policies',
            },
        ),
        migrations.CreateModel(
            name='MemberAccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('policy', models.JSONField(blank=True, help_text='Access Policy JSON', null=True, verbose_name='Policy')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iam_member_policies', to='users.member', verbose_name='Member')),
            ],
            options={
                'verbose_name': 'User Access Policy',
                'verbose_name_plural': 'User Access Policies',
            },
        ),
        migrations.CreateModel(
            name='GroupAccessPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('user_code', models.CharField(max_length=1024, unique=True, verbose_name='User Code')),
                ('policy', models.JSONField(blank=True, help_text='Access Policy JSON', null=True, verbose_name='Policy')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_policies', to='iam.group', verbose_name='Role')),
            ],
            options={
                'verbose_name': 'User Access Policy',
                'verbose_name_plural': 'User Access Policies',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='roles',
            field=models.ManyToManyField(related_name='iam_groups', to='iam.role'),
        ),
    ]

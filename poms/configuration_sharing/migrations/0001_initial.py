# Generated by Django 4.1.3 on 2022-12-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InviteToSharedConfigurationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('status', models.IntegerField(choices=[(0, 'Sent'), (1, 'Accepted'), (2, 'Declined')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SharedConfigurationFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('json_data', models.TextField(blank=True, null=True, verbose_name='json data')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('publicity_type', models.PositiveSmallIntegerField(choices=[(1, 'Public'), (2, 'Master User Only')], db_index=True, default=1, verbose_name='publicity type')),
            ],
        ),
    ]

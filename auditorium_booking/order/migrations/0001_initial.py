# Generated by Django 3.2.12 on 2023-03-31 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('payment', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
    ]

# Generated by Django 3.2.19 on 2024-01-12 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventFeedback',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback', models.CharField(max_length=50)),
                ('date_time', models.DateTimeField()),
                ('vend_id', models.IntegerField()),
            ],
            options={
                'db_table': 'event_feedback',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.2.3 on 2021-07-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0002_auto_20210722_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='addfriendmodel',
            name='has_seen',
            field=models.BooleanField(default=False),
        ),
    ]

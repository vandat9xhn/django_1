# Generated by Django 3.2.3 on 2021-07-25 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_personalsettingmodel_permission_see_interactive'),
        ('chat', '0002_auto_20210723_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_cr', to='user_profile.profilemodel'),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_o', to='user_profile.profilemodel'),
        ),
    ]

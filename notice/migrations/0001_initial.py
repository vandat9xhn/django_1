# Generated by Django 3.2.3 on 2021-07-23 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0006_personalsettingmodel_permission_see_interactive'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_id', models.URLField()),
                ('content', models.TextField()),
                ('status_seen', models.CharField(choices=[(0, 'sent'), (1, 'received'), (2, 'seen')], max_length=50)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('friend_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nt_fr', to='user_profile.profilemodel')),
                ('profile_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nt_pf', to='user_profile.profilemodel')),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-15 07:18

import _common.models.valid_field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0008_auto_20210613_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='post_to_where',
            field=models.CharField(choices=[('group', 'group'), ('user', 'user')], max_length=100),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='type_post',
            field=models.CharField(choices=[('post', 'post'), ('share', 'share'), ('picture', 'picture'), ('cover', 'cover')], default='post', max_length=50),
        ),
        migrations.AlterField(
            model_name='vidpicmodel',
            name='vid_pic',
            field=models.FileField(null=True, upload_to='media/facebook/post', validators=[_common.models.valid_field.valid_vid_pic]),
        ),
    ]

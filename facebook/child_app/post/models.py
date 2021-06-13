from django.db import models
#
from user_profile.models import ProfileModel
#
from _common.models.choices import CHOICES_PERMISSION_USER

# Create your models here.


CHOICES_POST_TO_WHERE = [
    ('group', 'group'),
    ('user', 'user'),
]

CHOICES_POST_TYPE = [
    ('post', 'post'),
    ('share', 'share'),
    ('picture', 'picture'),
    ('cover', 'cover'),
]


#


class PostModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_post')

    type_post = models.CharField(max_length=50, choices=CHOICES_POST_TYPE, default='post')
    post_to_where = models.CharField(max_length=100, choices=CHOICES_POST_TO_WHERE)
    post_to_id = models.IntegerField()

    content = models.TextField(null=True, default='', blank=True)
    permission = models.IntegerField(choices=CHOICES_PERMISSION_USER, default=0)

    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)


class PostShareModel(models.Model):
    post_model = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='p_p_sh')
    post_share_model = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='p_sh_p_sh')

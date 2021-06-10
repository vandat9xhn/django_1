from django.db import models
#
from user_profile import models as profile_models


# Create your models here.


CHOICES_POST_TO = [
    ('0', 'group'),
    ('1', 'user'),
]


#


class PostModel(models.Model):
    profile_model = models.ForeignKey(profile_models.ProfileModel, on_delete=models.CASCADE, related_name='pf_post')
    share_post_model = models.IntegerField(null=True)

    post_to_where = models.CharField(max_length=100, choices=CHOICES_POST_TO)
    post_to_id = models.IntegerField()
    content = models.TextField(null=True, default='')
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)

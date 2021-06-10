from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# Life event
class LifeEventModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    life_event = models.CharField(max_length=500)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


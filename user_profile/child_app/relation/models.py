from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# Relation
class RelationModel(models.Model):
    CHOICES_RELATION = [

    ]

    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    relation = models.CharField(max_length=100, choices=CHOICES_RELATION)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class FamilyModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    member = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='family_member')
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


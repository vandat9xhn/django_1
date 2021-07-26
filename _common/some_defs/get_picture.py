from user_profile.child_app.picture.models import PictureModel, CoverModel


#
def get_profile_picture_cover(profile_model_id, pic_cover_model):
    pic_models = pic_cover_model.objects.filter(profile_model=profile_model_id, is_active=True)

    if pic_models.exists():
        picture_url = pic_models.first().url
    else:
        picture_url = ''

    return picture_url


#
def get_profile_picture(profile_model_id):
    return get_profile_picture_cover(profile_model_id, PictureModel)


def get_profile_cover(profile_model_id):
    return get_profile_picture_cover(profile_model_id, CoverModel)

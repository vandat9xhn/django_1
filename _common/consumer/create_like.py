from django.core.exceptions import ObjectDoesNotExist


#


def create_like(queryset, user_id, type_like, data):
    try:
        like_model = queryset.get(profile_model=user_id, **data)
        if type_like == -1:
            like_model.delete()
        else:
            like_model.type_like = type_like
            like_model.save()

    except ObjectDoesNotExist:
        if type_like != -1:
            queryset.create(profile_model=user_id, **data, type_like=type_like)

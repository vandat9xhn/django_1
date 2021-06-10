from django.core.validators import ValidationError

#


def clean_content_vid_pic(content, vid_pic):
    if not content:
        if not vid_pic:
            raise ValidationError('Content and vid_pic are empty!')

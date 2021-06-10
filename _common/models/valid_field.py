from django.core.validators import FileExtensionValidator, ValidationError

#


def valid_vid_pic(file):
    valid_extension = FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg', 'mp4'])
    valid_extension.__call__(file)


def valid_number_phone(value):
    if len(str(value)) != 9:
        raise ValidationError('Wrong number phone')

from __default._info import user_id_arr, new_date_time, new_date

# 
profile_col_list = [
    'id',
    'is_online',
    'created_time',
]

profile_data = [(
    pk,
    0,
    new_date_time
) for pk in user_id_arr]

# 
name_col_list = [
    'profile_model_id',
    'first_name',
    'last_name',
    'updated_time',
]

name_data = [(
    pk,
    f'first name {pk}',
    f'last name {pk}',
    new_date_time
) for pk in user_id_arr]

# 
setting_col_list = [
    'profile_model_id',
    'permission_see_friend',
    'permission_add_friend',
    'permission_follow',
    'permission_post',
    'permission_see_interactive',
]

setting_data = [(
    pk,
    0,
    0,
    0,
    0,
    0
) for pk in user_id_arr]

#
# class GenderModel(models.Model):
gender_col_list = [
    'profile_model_id',
    'gender',
    'permission',
]

gender_data = [(
    pk,
    'male' if pk % 2 else 'female',
    0
) for pk in user_id_arr]

# class BirthModel(models.Model):
birth_col_list = [
    'profile_model_id',
    'birth',
    'permission',
]

birth_data = [(
    pk,
    new_date,
    0
) for pk in user_id_arr]

# class LanguageModel(models.Model):
lang_col_list = [
    'profile_model_id',
    'lang',
    'permission',
]

lang_data = [(
    pk,
    '',
    0
) for pk in user_id_arr]

# class MailModel(models.Model):
mail_col_list = [
    'profile_model_id',
    'mail',
    'permission',
]

mail_data = [(
    pk,
    f'iloveyou_{pk}@gmail.com',
    0
) for pk in user_id_arr]

# 
# class RelationModel(models.Model):
relation_col_list = [
    'profile_model_id',
    'relation',
    'permission',
]

relation_data = [(
    pk,
    '',
    0
) for pk in user_id_arr]

# 
# class AboutYouModel(models.Model):
you_col_list = [
    'profile_model_id',
    'you',
    'permission',
]

you_data = [(
    pk,
    '',
    0
) for pk in user_id_arr]

# class HobbyModel(models.Model):
hobby_col_list = [
    'profile_model_id',
    'hobby',
    'permission',
]

hobby_data = [(
    pk,
    '',
    0
) for pk in user_id_arr]

#
default_profile_arr = [
    {
        'model_name': 'user_profile_profilemodel',
        'col_list': profile_col_list,
        'data': profile_data,
    },
    {
        'model_name': 'user_profile_namemodel',
        'col_list': name_col_list,
        'data': name_data,
    },
    {
        'model_name': 'user_profile_personalsettingmodel',
        'col_list': setting_col_list,
        'data': setting_data,
    },

    {
        'model_name': 'user_profile_gendermodel',
        'col_list': gender_col_list,
        'data': gender_data,
    },
    {
        'model_name': 'user_profile_birthmodel',
        'col_list': birth_col_list,
        'data': birth_data,
    },
    {
        'model_name': 'user_profile_languagemodel',
        'col_list': lang_col_list,
        'data': lang_data,
    },

    {
        'model_name': 'user_profile_mailmodel',
        'col_list': mail_col_list,
        'data': mail_data,
    },

    {
        'model_name': 'user_profile_relationmodel',
        'col_list': relation_col_list,
        'data': relation_data,
    },

    {
        'model_name': 'user_profile_aboutyoumodel',
        'col_list': you_col_list,
        'data': you_data,
    },
    {
        'model_name': 'user_profile_hobbymodel',
        'col_list': hobby_col_list,
        'data': hobby_data,
    },
]

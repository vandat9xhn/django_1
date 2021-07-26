from django.contrib.auth.hashers import make_password
#
from __default._info import user_id_arr, new_date_time


#
user_col_list = [
    'id',
    'username',
    'password',
    'email',
    'first_name',
    'last_name',
    'is_staff',
    'is_superuser',
    'is_active',
    'date_joined',
]

user_data = [(
    pk,
    f'iloveyou_{pk}',
    make_password('iloveyou1234'),
    f'iloveyou_{pk}@gmail.com',
    f'first name {pk}',
    f'last name {pk}',
    0,
    0,
    1,
    new_date_time,
) for pk in user_id_arr]


#
refresh_col_list = [
    'profile_model_id',
    'refresh_token',
    'updated_time',
]

refresh_data = [(
    pk,
    '',
    new_date_time,
) for pk in user_id_arr]

#


default_account_arr = [
    {
        'model_name': 'auth_user',
        'col_list': user_col_list,
        'data': user_data,
    },
    {
        'model_name': 'account_refreshtokenmodel',
        'col_list': refresh_col_list,
        'data': refresh_data,
    },

]

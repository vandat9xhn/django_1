from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id, post_id_arr

#
post_col_list = [
    'id',
    'profile_model_id',

    'type_post',
    'post_to_where',
    'post_to_id',

    'content',
    'permission',

    'created_time',
    'updated_time',
]

post_data = [(
    pk,
    random_user_id(),

    'post',
    'user',
    random_user_id(),

    f'content {pk}',
    0,

    new_date_time,
    new_date_time,
) for pk in post_id_arr]

#
default_post_arr = [
    {
        'model_name': 'facebook_postmodel',
        'col_list': post_col_list,
        'data': post_data,
    },
]

from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#
like_col_list = [
    'profile_model_id',
    'post_model_id',
    'type_like',
]

like_data = [(
    random_user_id(),
    random_post_id(),
    random_id(0, 6)
)]

#
share_col_list = [
    'profile_model_id',
    'post_model_id',
    'count',
]

share_data = [(
    random_user_id(),
    random_post_id(),
    1
)]

#
default_like_share_arr = [
    {
        'model_name': 'facebook_likemodel',
        'col_list': like_col_list,
        'data': like_data,
    },
    {
        'model_name': 'facebook_sharemodel',
        'col_list': share_col_list,
        'data': share_data,
    },
]

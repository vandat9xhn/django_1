from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id

#
notice_col_list = [
    'profile_model_id',
    'friend_model_id',

    'link_id',
    'content',
    'status_seen',
    'updated_time',
]

notice_data = [(
    user_id_arr[0],
    user_id_arr[1],

    f'/posts/{random_post_id()}',
    'has liked your post',
    0,
    new_date_time
)]

#
default_notice_arr = [
    {
        'model_name': 'notice_noticemodel',
        'col_list': notice_col_list,
        'data': notice_data,
    },
]

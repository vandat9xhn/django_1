from __default._info import user_id_arr, new_date_time, random_user_id

#
friend_col_list = [
    'profile_model_id',
    'friend_model_id',
    'is_follow',
    'updated_time',
    'created_time',
]

friend_data = [(
    user_id_arr[0],
    user_id_arr[1],
    1,
    new_date_time,
    new_date_time
), (
    user_id_arr[1],
    user_id_arr[0],
    1,
    new_date_time,
    new_date_time
)]

#
add_friend_col_list = [
    'requester_id',
    'receiver_id',
    'has_seen',
    'created_time',
]

add_friend_data = [(
    user_id_arr[0],
    user_id_arr[2],
    0,
    new_date_time
)]

#
friend_remove_col_list = [
    'profile_model_id',
    'friend_model_id',
]

friend_remove_data = [(
    user_id_arr[1],
    user_id_arr[2]
)]

#
default_friend_arr = [
    {
        'model_name': 'friend_friendmodel',
        'col_list': friend_col_list,
        'data': friend_data,
    },
    {
        'model_name': 'friend_addfriendmodel',
        'col_list': add_friend_col_list,
        'data': add_friend_data,
    },
    {
        'model_name': 'friend_friendremovemodel',
        'col_list': friend_remove_col_list,
        'data': friend_remove_data,
    }
]

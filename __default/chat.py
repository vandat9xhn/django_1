from __default._info import user_id_arr, new_date_time

#
room_chat = f'{user_id_arr[0]}_{user_id_arr[1]}'
mess_id_arr = range(100, 104)

#
room_col_list = [
    'room_chat',
    'is_group',
    'owner_id',
    'creator_id',
    'created_time',
    'updated_time',
]

room_data = [(
    room_chat,
    0,
    user_id_arr[0],
    user_id_arr[0],
    new_date_time,
    new_date_time
)]

#
room_user_col_list = [
    'room_model_id',
    'profile_model_id',

    'is_notice',
    'on_chat',
    'on_input',

    'begin_mess',
    'last_mess',
    'last_receive',
    'last_seen',

    'joined_time',
]

room_user_data = [(
    room_chat,
    pk,

    1,
    0,
    0,

    0,
    0,
    0,
    0,

    new_date_time,
) for pk in user_id_arr[0:2]]

#
mess_col_list = [
    'id',
    'room_model_id',
    'profile_model_id',
    'message',
    'created_time',
]

mess_data = [(
    pk,
    room_chat,
    user_id_arr[0] if pk % 2 else user_id_arr[1],
    f'This is message ({pk})',
    new_date_time
) for pk in mess_id_arr]

#
default_chat_arr = [
    {
        'model_name': 'chat_roommodel',
        'col_list': room_col_list,
        'data': room_data,
    },
    {
        'model_name': 'chat_roomusermodel',
        'col_list': room_user_col_list,
        'data': room_user_data,
    },
    {
        'model_name': 'chat_messagemodel',
        'col_list': mess_col_list,
        'data': mess_data,
    },
]

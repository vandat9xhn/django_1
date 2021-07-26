from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

# 
history_col_list = [
    'post_model_id',
    'content',
    'created_time',
]

history_data = [(
    random_post_id(),
    'content',
    new_date_time,
)]

#
default_history_arr = [
    {
        'model_name': 'facebook_historymodel',
        'col_list': history_col_list,
        'data': history_data,
    },
]

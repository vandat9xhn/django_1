from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#
vid_pic_id = 10

# 
vid_pic_col_list = [
    'id',
    'post_model_id',
    'content',
    'vid_pic',
]

vid_pic_data = [(
    vid_pic_id,
    random_post_id(),
    'content',
    'media/banner_phone.jpg'
)]

#
vid_pic_like_col_list = [
    'profile_model_id',
    'vid_pic_model_id',
    'type_like',
]

vid_pic_like_data = [(
    random_user_id(),
    vid_pic_id,
    random_id(0, 6)
)]

#
vid_pic_share_col_list = [
    'profile_model_id',
    'vid_pic_model_id',
    'count',
]

vid_pic_share_data = [(
    random_user_id(),
    vid_pic_id,
    1
)]

# 
default_like_share_arr = [
    {
        'model_name': 'facebook_vidpicmodel',
        'col_list': vid_pic_col_list,
        'data': vid_pic_data,
    },
    {
        'model_name': 'facebook_vidpiclikemodel',
        'col_list': vid_pic_like_col_list,
        'data': vid_pic_like_data,
    },
    {
        'model_name': 'facebook_vidpicsharemodel',
        'col_list': vid_pic_share_col_list,
        'data': vid_pic_share_data,
    },
]

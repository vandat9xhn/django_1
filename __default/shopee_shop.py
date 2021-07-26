from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#
shop_id_arr = user_id_arr

#
shop_col_list = [
    'id',
    'profile_model_id',
    'name',
    'picture',
    'banner',
    'address',
    'info',

    'created_time',
    'updated_time',
]

shop_data = [(
    pk,
    pk,
    f'name {pk}',
    'media/banner_phone.jpg',
    'media/banner_phone.jpg',
    f'address {pk}',
    f'info {pk}',

    new_date_time,
    new_date_time,
) for pk in shop_id_arr]

#
shop_vid_pic_col_list = [
    'shop_model_id',
    'vid_pic',
]

shop_vid_pic_data = [(
    pk,
    'media/banner_phone.jpg'
) for pk in shop_id_arr] * 4

#
default_fashion_arr = [
    {
        'model_name': 'shopee_shopmodel',
        'col_list': shop_col_list,
        'data': shop_data,
    },
    {
        'model_name': 'shopee_shopvidpicmodel',
        'col_list': shop_vid_pic_col_list,
        'data': shop_vid_pic_data,
    },
]

from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#
product_id_arr = list(range(1, 6))
product_count_arr = len(product_id_arr)

#
product_col_list = [
    'id',
    'shop_model_id',
    'group_model_id',

    'brand',
    'type',
    'hashtag',
    'name',
    'new_price',
    'old_price',
    'discount',
    'description',
    'total',

    'sold',
    'rate',

    'created_time',
    'updated_time',
]

product_data = [(
    pk,
    random_user_id(),
    None,

    f'brand',
    f'type',
    f'hashtag',
    f'name {pk}',
    random_id(10, 1000) * 1000,
    random_id(10, 1000) * 1000,
    random_id(1, 10),
    f'description {pk}',
    random_id(100, 200),

    random_id(0, 100),
    random_id(10, 50) / 10,

    new_date_time,
    new_date_time,
) for pk in product_id_arr]

#
product_vid_pic_col_list = [
    'product_model_id',
    'vid_pic',
]

product_vid_pic_data = [(
    pk,
    'media/banner_phone.jpg'
) for pk in product_id_arr] * 4

#
product_cmt_col_list = [
    'profile_model_id',
    'product_model_id',
    'content',
    'created_time',
]

product_cmt_data = [(
    random_user_id(),
    pk,
    f'content {pk}',
    new_date_time
) for pk in product_id_arr * 4]

#
product_rate_col_list = [
    'profile_model_id',
    'product_model_id',
    'content',
    'num_rate',
    'created_time',
]

product_rate_data = [(
    random_user_id(),
    pk,
    f'content {pk}',
    random_id(1, 5),
    new_date_time
) for pk in product_id_arr * 4]

#
default_fashion_arr = [
    {
        'model_name': 'shopee_productmodel',
        'col_list': product_col_list,
        'data': product_data,
    },
    {
        'model_name': 'shopee_productvidpicmodel',
        'col_list': product_vid_pic_col_list,
        'data': product_vid_pic_data,
    },
    {
        'model_name': 'shopee_productcmtmodel',
        'col_list': product_cmt_col_list,
        'data': product_cmt_data,
    },
    {
        'model_name': 'shopee_productratemodel',
        'col_list': product_rate_col_list,
        'data': product_rate_data,
    },
]

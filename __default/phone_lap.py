from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#

#
phone_lap_id_arr = range(1, 5)

#
phone_lap_col_list = [
    'name',
    'type_product',
    'new_price',
    'old_price',

    'cpu',
    'os',
    'ram',
    'internal_memory',
    'camera',
    'memory_stick',

    'special',
    'cpu_type',
    'cpu_lv',
    'ram_lv',
    'internal_memory_lv',
    'camera_type',
    'memory_stick_lv',

    'in_stock',
    'discount',
    'installment',

    'gift',
    'product_sets',
    'promotion',
]

phone_lap_data = [(
    f'name {pk}',
    f'type_product {pk}',
    'new_price',
    'old_price',

    f'cpu {pk}',
    'android' if pk % 2 else 'ios',
    f'{random_id(1, 32)}G',
    f'{random_id(4, 256)}G',
    f'camera {pk}',
    f'{random_id(4, 256)}G',

    f'special {pk}',
    random_id(0, 3),
    random_id(0, 2),
    random_id(0, 4),
    random_id(0, 5),
    random_id(0, 2),
    random_id(0, 3),

    'In stock',
    1,
    0,

    f'gift {pk}',
    f'product_sets {pk}',
    f'promotion {pk}',
) for pk in phone_lap_id_arr]

#
vid_pic_col_list = [
    'phone_lap_model_id',
    'vid_pic',
]

vid_pic_data = [(
    pk,
    'media/phone_lap/phone_jpg.jpg'
) for pk in phone_lap_id_arr] * 6

#
# type_col_list = [
#     'phone_lap_model_id',
#     'url',
#     'color',
#     'title',
# ]

#
default_phone_lap_arr = [
    {
        'model_name': 'phone_lap_phonelapmodel',
        'col_list': phone_lap_col_list,
        'data': phone_lap_data,
    },
{
        'model_name': 'phone_lap_vidpicmodel',
        'col_list': vid_pic_col_list,
        'data': vid_pic_data,
    },
]

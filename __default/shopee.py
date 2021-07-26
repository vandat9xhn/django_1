from __default._info import user_id_arr, new_date_time, random_user_id, random_post_id, random_id

#
voucher_id_arr = range(1, 8)
transport_id_arr = range(1, 5)

#
payment_col_list = [
    'name',
]

payment_data = [
    ('COD',),
    ('BANK',),
    ('VISA',),
    ('MOMO',),
]

# 
voucher_col_list = [
    'id',
    'name',
    'cost',
    'img',
    'info',

    'min_amount',
    'expires',
    'total_num',
    'count_user',
]

voucher_data = [(
    pk,
    f'name {pk}',
    random_id(10, 35) * 1000,
    'media/banner_phone.jpg',
    f'info {pk}',

    random_id(10, 35) * 10000,
    random_id(1, 10),
    100,
    0,
) for pk in voucher_id_arr]

#
voucher_payment_col_list = [
    'voucher_model_id',
    'payment_model_id',
]

voucher_payment_data = [(
    pk,
    None
) for pk in voucher_id_arr]

# 
transport_col_list = [
    'id',
    'name',
    'info',
    'created_time',
    'updated_time',
]

transport_data = [(
    pk,
    f'name {pk}',
    f'info {pk}',
    new_date_time,
    new_date_time
) for pk in transport_id_arr]

# 
transport_price_col_list = [
    'transport_model_id',
    'name',
    'info',
    'price',
    'created_time',
    'updated_time',
]

transport_price_data = [(
    pk,
    f'name {pk}',
    f'info {pk}',
    random_id(10, 50) * 1000,
    new_date_time,
    new_date_time
) for pk in transport_id_arr]

#
default_fashion_arr = [
    {
        'model_name': 'shopee_paymentmodel',
        'col_list': payment_col_list,
        'data': payment_data,
    },
    {
        'model_name': 'shopee_vouchermodel',
        'col_list': voucher_col_list,
        'data': voucher_data,
    },
    {
        'model_name': 'shopee_transportmodel',
        'col_list': transport_col_list,
        'data': transport_data,
    },
    {
        'model_name': 'shopee_transportpricemodel',
        'col_list': transport_price_col_list,
        'data': transport_price_data,
    },
]

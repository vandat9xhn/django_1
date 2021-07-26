from __default._info import user_id_arr, new_date_time, random_user_id

#
city_id_arr = range(1, 3)

#
city_col_list = [
    'id',
    'profile_model_id',

    'city',
    'street',
    'bg_color',
    'quote',
    'image',

    'created_time',
    'updated_time',
]

city_data = [(
    pk,
    random_user_id(),

    f'City {pk}',
    f'Street {pk}',
    'bg-primary.text-primary',
    f'Quote {pk}',
    'media/city/beautiful_place.png',

    new_date_time,
    new_date_time
) for pk in city_id_arr]

#
history_col_list = [
    'city_model_id',

    'city',
    'street',
    'quote',
    'bg_color',
    'image',

    'created_time',
]

history_data = [(
    city_id_arr[0],

    f'City history',
    None,
    None,
    'bg-primary.text-primary',
    None,

    new_date_time
)]

#
default_city_arr = [
    {
        'model_name': 'city_citymodel',
        'col_list': city_col_list,
        'data': city_data,
    },
    {
        'model_name': 'city_historymodel',
        'col_list': history_col_list,
        'data': history_data,
    },
]

from datetime import datetime
import random

#
user_id_min = 20
user_id_max = 23

post_id_min = 10
post_id_max = 15

new_date_time = datetime.now()
new_date = datetime.now().date()
user_id_arr = range(user_id_min, user_id_max)

post_id_arr = range(post_id_min, post_id_max)


#
def random_id(min_id, max_id):
    return random.randint(min_id, max_id)


def random_user_id():
    return random_id(user_id_min, user_id_max)


def random_post_id():
    return random_id(post_id_min, post_id_max)

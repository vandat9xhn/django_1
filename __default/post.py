import sqlite3
# 
import random
from datetime import datetime


#


def repeat_str(string, time, delimiter=','):
    return delimiter.join([string] * time)


def get_cursor():
    conn = sqlite3.connect('D:\\web\\react-django\\react_django_1\\db.sqlite3')
    cur = conn.cursor()
    return cur


def insert_into_sqlite3(cur, table_name, count_field, data):
    cur.executemany(f'Insert Into {table_name} Values(' + repeat_str('?', count_field) + ')', data)


def close_sqlite3(cur):
    cur.close()


#
def make_default_post():
    make_post()


#


def make_post():
    cur = get_cursor()

    data_post = []
    data_like = []
    data_share = []
    
    data_vid_pic = []
    data_vid_pic_cmt = []
    data_vid_pic_cmt_like = []
    data_vid_pic_sub = []
    data_vid_pic_sub_like = []
    
    data_cmt = []
    data_cmt_like = []
    data_sub = []
    data_sub_like = []
    
    for i in range(50):
        new_data_like = make_like(i)
        new_data_share = make_share(i)

        new_data_vid_pic, new_data_vid_pic_cmt, new_data_vid_pic_cmt_like, new_data_vid_pic_sub,\
        new_data_vid_pic_sub_like = make_vid_pic(i)

        new_data_cmt, new_data_cmt_like, new_data_sub, new_data_sub_like = make_comment(i)

        pk = i
        profile_model = random.randint(1, 6)
        share_post_model = 0

        post_to_where = '1'
        post_to_id = 1
        content = 'a a asd asd'
        created_time = datetime.now()
        updated_time = datetime.now()
        
        data_post += [
            pk,
            profile_model,
            share_post_model,
            post_to_where,
            post_to_id,
            content,
            created_time,
            updated_time,
        ]

    data_post += [
        1,
        1,
        1,
        '1',
        2,
        'share',
        datetime.now(),
        datetime.now(),
    ]
    
    insert_into_sqlite3(cur, 'facebook_postmodel', 8, data_post)

    close_sqlite3(cur)


def make_vid_pic(post_id):
    return []


def make_like(post_id):
    return []


def make_share(post_id):
    return []


def make_comment(post_id):
    return []


def make_history(post_id):
    return []


#


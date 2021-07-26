#
from __default._common import get_connection, insert_into_sqlite3, commit_sqlite3, close_sqlite3
#
from __default import account, chat, city, facebook_history, facebook_like_share, facebook_post, facebook_vid_pic, \
    friend, notice, phone_lap, shopee, shopee_product, shopee_shop, user_profile

#
default_arr = [
    *account.default_account_arr,
    *chat.default_chat_arr,
    *city.default_city_arr,

    *facebook_history.default_history_arr,
    *facebook_like_share.default_like_share_arr,
    *facebook_post.default_post_arr,
    *facebook_vid_pic.default_like_share_arr,

    *friend.default_friend_arr,
    *notice.default_notice_arr,
    *phone_lap.default_phone_lap_arr,

    *shopee.default_fashion_arr,
    *shopee_product.default_fashion_arr,
    *shopee_shop.default_fashion_arr,

    *user_profile.default_profile_arr,
]


# import importlib
# from __default._make_default import make_default
def make_default():
    conn = get_connection()

    for default_data in default_arr:
        print(default_data['model_name'])

        insert_into_sqlite3(
            conn,
            default_data['model_name'],
            default_data['col_list'],
            default_data['data']
        )

    commit_sqlite3(conn)
    close_sqlite3(conn)

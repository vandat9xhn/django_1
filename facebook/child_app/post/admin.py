from django.contrib import admin
#
from .models import PostModel
from .vid_pic.models import VidPicModel, VidPicLikeModel, VidPicShareModel, VidPicHistoryModel
from .like_share.models import LikeModel, ShareModel
from .history.models import HistoryModel, HistoryVidPicDelModel, HistoryVidPicCreateModel

from .comment.models import CommentModel, CmtLikeModel, CmtHistoryModel
from .comment.sub.models import SubModel, SubLikeModel, SubHistoryModel

from .vid_pic.comment.models import VidPicCmtModel, VidPicCmtLikeModel, VidPicCmtHistoryModel
from .vid_pic.comment.sub.models import VidPicSubModel, VidPicSubHistoryModel, VidPicSubLikeModel

# Register your models here.

all_models = [
    PostModel,
    VidPicModel, VidPicLikeModel, VidPicShareModel, VidPicHistoryModel,
    LikeModel, ShareModel,
    HistoryModel, HistoryVidPicDelModel, HistoryVidPicCreateModel,

    CommentModel, CmtLikeModel, CmtHistoryModel,
    SubModel, SubLikeModel, SubHistoryModel,

    VidPicCmtModel, VidPicCmtLikeModel, VidPicCmtHistoryModel,
    VidPicSubModel, VidPicSubHistoryModel, VidPicSubLikeModel
]

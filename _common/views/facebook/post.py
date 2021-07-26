from rest_framework.generics import ListAPIView
#
from friend.models import friend_relative_num
#
from facebook.child_app.post.models import PostModel
from facebook.child_app.post.comment.models import CommentModel
from facebook.child_app.post.comment.sub.models import SubModel

from facebook.child_app.post.vid_pic.models import VidPicModel
from facebook.child_app.post.vid_pic.comment.models import VidPicCmtModel
from facebook.child_app.post.vid_pic.comment.sub.models import VidPicSubModel


# --------------


#
class PostPermissionViewL(ListAPIView):

    def has_permission_queryset(self, follow_model):
        post_model = self.get_post_model(follow_model)

        relative = friend_relative_num(
            self.request.user.id,
            post_model.profile_model.id
        )

        if relative >= post_model.permission:
            return True

        return False

    def get_post_model(self, follow_model):
        return follow_model


# ------------

#
def get_like_queryset(request, queryset):
    type_like = request.query_params['type_like']

    if type_like == '-1':
        return queryset
    else:
        return queryset.filter(type_like=type_like)

# ------------


class FollowPostViewL(PostPermissionViewL):

    def get_queryset(self):
        post_id = self.request.query_params.get('post_model')
        post_model = PostModel.objects.get(id=post_id)

        if self.has_permission_queryset(post_model):
            return self.queryset.filter(post_model=post_id)

        return []


class FollowCommentViewL(PostPermissionViewL):

    def get_queryset(self):
        comment_id = self.request.query_params.get('comment_model')
        comment_model = CommentModel.objects.get(id=comment_id)

        if self.has_permission_queryset(comment_model):
            return self.queryset.filter(comment_model=comment_id)

        return []

    def get_post_model(self, follow_model):
        return follow_model.post_model


class FollowSubViewL(PostPermissionViewL):

    def get_queryset(self):
        sub_id = self.request.query_params.get('sub_model')
        sub_model = SubModel.objects.get(id=sub_id)

        if self.has_permission_queryset(sub_model):
            return self.queryset.filter(sub_model=sub_id)

        return []

    def get_post_model(self, follow_model):
        return follow_model.comment_model.post_model


#
class FollowVidPicViewL(PostPermissionViewL):

    def get_queryset(self):
        vid_pic_id = self.request.query_params.get('vid_pic_model')
        vid_pic_model = VidPicModel.objects.get(id=vid_pic_id)

        if self.has_permission_queryset(vid_pic_model):
            return self.queryset.filter(vid_pic_model=vid_pic_id)

        return []

    def get_post_model(self, follow_model):
        return follow_model.post_model


class FollowVidPicCmtViewL(PostPermissionViewL):

    def get_queryset(self):
        comment_id = self.request.query_params.get('vid_pic_cmt_model')
        comment_model = VidPicCmtModel.objects.get(id=comment_id)

        if self.has_permission_queryset(comment_model):
            return self.queryset.filter(comment_model=comment_id)

        return []

    def get_post_model(self, follow_model):
        return follow_model.vid_pic_model.post_model


class FollowVidPicSubViewL(PostPermissionViewL):

    def get_queryset(self):
        sub_id = self.request.query_params.get('vid_pic_sub_model')
        sub_model = VidPicSubModel.objects.get(id=sub_id)

        if self.has_permission_queryset(sub_model):
            return self.queryset.filter(sub_model=sub_id)

        return []

    def get_post_model(self, follow_model):
        return follow_model.comment_model.vid_pic_model.post_model

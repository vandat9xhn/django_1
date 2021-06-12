from rest_framework.generics import ListAPIView


#


class FollowPostViewL(ListAPIView):

    def get_queryset(self):
        post_id = self.request.query_params.get('post_model')

        return self.queryset.filter(post_model=post_id)


class FollowVidPicViewL(ListAPIView):

    def get_queryset(self):
        vid_pic_id = self.request.query_params.get('vid_pic_model')

        return self.queryset.filter(vid_pic_model=vid_pic_id)

from ..user_create import UserCreateView


#


class CommentSubViewC(UserCreateView):

    def has_permission_create(self):
        content = self.request.data.get('content')
        vid_pic = self.request.data.get('vid_pic')

        if content or vid_pic:
            return True

        return False

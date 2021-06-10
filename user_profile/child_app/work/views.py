#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class WorkView:
    serializer_class = serializers.WorkSerializer
    queryset = models.WorkModel


class SchoolView:
    serializer_class = serializers.SchoolSerializer
    queryset = models.SchoolModel


class UniversityView:
    serializer_class = serializers.UniversitySerializer
    queryset = models.UniversityModel


# -------------------------


#
class WorkViewC(WorkView, UserCreateView):
    pass


class WorkViewUD(WorkView, UserUpdateView, UserDestroyView):
    pass


#
class SchoolViewC(SchoolView, UserCreateView):
    pass


class SchoolViewUD(SchoolView, UserUpdateView, UserDestroyView):
    pass


#
class UniversityViewC(UniversityView, UserCreateView):
    pass


class UniversityViewUD(UniversityView, UserUpdateView, UserDestroyView):
    pass

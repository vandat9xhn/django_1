from django.contrib import admin
#
from .models import ProfileModel, NameModel, PersonalSettingModel
#
from .child_app.you.models import HobbyModel, OtherNameModel, AboutYouModel
from .child_app.work.models import WorkModel, SchoolModel, UniversityModel
from .child_app.basis.models import BirthModel, LanguageModel, GenderModel
from .child_app.placed.models import CityModel, TownModel
from .child_app.contact.models import MailModel, PhoneModel, AddressModel
from .child_app.relation.models import RelationModel, FamilyModel
from .child_app.life_event.models import LifeEventModel
from .child_app.picture.models import PictureModel, CoverModel

# Register your models here.


all_models = [
    ProfileModel, NameModel, PersonalSettingModel,

    HobbyModel, OtherNameModel, AboutYouModel,
    WorkModel, SchoolModel, UniversityModel,
    BirthModel, LanguageModel, GenderModel,
    CityModel, TownModel,
    MailModel, PhoneModel, AddressModel,
    RelationModel, FamilyModel,
    LifeEventModel,
    PictureModel, CoverModel,
]

#
for model in all_models:
    admin.site.register(model)

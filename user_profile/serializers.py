#
from rest_framework.serializers import SerializerMethodField
#
from .models import ProfileModel, NameModel, PersonalSettingModel
#
from .child_app.picture.models import PictureModel, CoverModel

from .child_app.basis import serializers as basis_ser
from .child_app.life_event import serializers as life_ser
from .child_app.contact import serializers as contact_ser
from .child_app.placed import serializers as placed_ser
from .child_app.relation import serializers as relation_ser
from .child_app.work import serializers as work_ser
from .child_app.you import serializers as you_ser
#
from _common.serializers import data_field, permission_field


# 


class DataProfilePermissionSerializerL(permission_field.DataPermissionSerializerL):

    def get_data_profile_permission_l(self, serializer, queryset, instance):
        return self.get_data_permission_l(serializer, queryset, instance.id)


#


class NameSerializer(data_field.DataSerializerR):
    name_field = 'pf_name[]'
    #

    class Meta:
        model = NameModel
        fields = '__all__'


#
class ProfileSerializer(DataProfilePermissionSerializerL):
    name_field = 'profile[]'
    #
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    picture = SerializerMethodField()
    cover = SerializerMethodField()
    #
    gender_arr = SerializerMethodField()
    birth_arr = SerializerMethodField()
    lang_arr = SerializerMethodField()

    life_arr = SerializerMethodField()

    mail_arr = SerializerMethodField()
    phone_arr = SerializerMethodField()
    address_arr = SerializerMethodField()

    town_arr = SerializerMethodField()
    city_arr = SerializerMethodField()

    family_arr = SerializerMethodField()
    relation_arr = SerializerMethodField()

    work_arr = SerializerMethodField()
    school_arr = SerializerMethodField()
    university_arr = SerializerMethodField()

    hobby_arr = SerializerMethodField()
    you_arr = SerializerMethodField()
    other_name_arr = SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = ProfileModel

    #
    @staticmethod
    def get_first_name(instance):
        return NameModel.objects.get(profile_model=instance.id).first_name

    @staticmethod
    def get_last_name(instance):
        return NameModel.objects.get(profile_model=instance.id).last_name

    @staticmethod
    def get_picture(instance):
        return PictureModel.objects.get(profile_model=instance.id, is_active=True).url

    @staticmethod
    def get_cover(instance):
        return CoverModel.objects.get(profile_model=instance.id, is_active=True).url

    # basis
    def get_gender_arr(self, instance):
        return self.get_data_profile_permission_l(
            basis_ser.GenderSerializer,
            basis_ser.models.GenderModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_birth_arr(self, instance):
        return self.get_data_profile_permission_l(
            basis_ser.BirthSerializer,
            basis_ser.models.BirthModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_lang_arr(self, instance):
        return self.get_data_profile_permission_l(
            basis_ser.LanguageSerializer,
            basis_ser.models.LanguageModel.objects.filter(profile_model=instance.id),
            instance
        )

    # life
    def get_life_arr(self, instance):
        return self.get_data_profile_permission_l(
            life_ser.LifeEventSerializer,
            life_ser.models.LifeEventModel.objects.filter(profile_model=instance.id),
            instance
        )

    # contact
    def get_mail_arr(self, instance):
        return self.get_data_profile_permission_l(
            contact_ser.MailSerializer,
            contact_ser.models.MailModel.objects.filter(profile_model=instance.id),
            instance
        )
    
    def get_phone_arr(self, instance):
        return self.get_data_profile_permission_l(
            contact_ser.PhoneSerializer,
            contact_ser.models.PhoneModel.objects.filter(profile_model=instance.id),
            instance
        )
    
    def get_address_arr(self, instance):
        return self.get_data_profile_permission_l(
            contact_ser.AddressSerializer,
            contact_ser.models.AddressModel.objects.filter(profile_model=instance.id),
            instance
        )

    # placed
    def get_town_arr(self, instance):
        return self.get_data_profile_permission_l(
            placed_ser.TownSerializer,
            placed_ser.models.TownModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_city_arr(self, instance):
        return self.get_data_profile_permission_l(
            placed_ser.CitySerializer,
            placed_ser.models.CityModel.objects.filter(profile_model=instance.id),
            instance
        )

    # relationships
    def get_family_arr(self, instance):
        return self.get_data_profile_permission_l(
            relation_ser.FamilySerializer,
            relation_ser.models.FamilyModel.objects.filter(profile_model=instance.id),
            instance
        )
    
    def get_relation_arr(self, instance):
        return self.get_data_profile_permission_l(
            relation_ser.RelationSerializer,
            relation_ser.models.RelationModel.objects.filter(profile_model=instance.id),
            instance
        )

    # contact
    def get_work_arr(self, instance):
        return self.get_data_profile_permission_l(
            work_ser.WorkSerializer,
            work_ser.models.WorkModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_school_arr(self, instance):
        return self.get_data_profile_permission_l(
            work_ser.SchoolSerializer,
            work_ser.models.SchoolModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_university_arr(self, instance):
        return self.get_data_profile_permission_l(
            work_ser.UniversitySerializer,
            work_ser.models.UniversityModel.objects.filter(profile_model=instance.id),
            instance
        )

    # hobby
    def get_hobby_arr(self, instance):
        return self.get_data_profile_permission_l(
            you_ser.HobbySerializer,
            you_ser.models.HobbyModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_you_arr(self, instance):
        return self.get_data_profile_permission_l(
            you_ser.AboutYouSerializer,
            you_ser.models.AboutYouModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_other_name_arr(self, instance):
        return self.get_data_profile_permission_l(
            you_ser.OtherNameSerializer,
            you_ser.models.OtherNameModel.objects.filter(profile_model=instance.id),
            instance
        )


class PersonalSettingSerializer(data_field.FieldSerializer):
    name_field = 'personal_setting[]'

    class Meta:
        model = PersonalSettingModel
        fields = '__all__'

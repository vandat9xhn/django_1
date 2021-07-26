#
from rest_framework.serializers import SerializerMethodField
#
from .models import ProfileModel, NameModel, PersonalSettingModel
#
from .child_app.basis import serializers as basis_ser
from .child_app.life_event import serializers as life_ser
from .child_app.contact import serializers as contact_ser
from .child_app.placed import serializers as placed_ser
from .child_app.relation import serializers as relation_ser
from .child_app.work import serializers as work_ser
from .child_app.you import serializers as you_ser
#
from _common.serializers import data_field, permission_field, custom_field
from _common.some_defs.get_picture import get_profile_picture, get_profile_cover


# 


class DataProfilePermissionSerializer(permission_field.DataPermissionSerializerL):

    def get_data_profile_permission_l(self, serializer, queryset, instance):
        return self.get_data_permission_l(serializer, queryset, instance.id)

    def get_data_profile_permission_r(self, serializer, queryset, instance):
        data = self.get_data_permission_l(serializer, queryset, instance.id)

        if len(data):
            return self.get_data_permission_l(serializer, queryset, instance.id)[0]

        return {}


#


class NameSerializer(data_field.DataSerializerR):
    name_field = 'pf_names'
    #

    class Meta:
        model = NameModel
        fields = '__all__'


#
class ProfileSerializer(DataProfilePermissionSerializer):
    name_field = 'profiles'
    #
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    picture = SerializerMethodField()
    cover = SerializerMethodField()
    #
    gender_obj = SerializerMethodField()
    birth_obj = SerializerMethodField()
    # lang_obj = SerializerMethodField()
    #
    # life_arr = SerializerMethodField()
    #
    # mail_obj = SerializerMethodField()
    # phone_arr = SerializerMethodField()
    # address_arr = SerializerMethodField()
    #
    # town_arr = SerializerMethodField()
    # city_arr = SerializerMethodField()
    #
    # family_arr = SerializerMethodField()
    # relationship_obj = SerializerMethodField()
    #
    # work_arr = SerializerMethodField()
    # school_arr = SerializerMethodField()
    # university_arr = SerializerMethodField()
    #
    # hobby_obj = SerializerMethodField()
    # you_obj = SerializerMethodField()
    # other_name_arr = SerializerMethodField()

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
        return get_profile_picture(instance.id)

    @staticmethod
    def get_cover(instance):
        return get_profile_cover(instance.id)

    # basis
    def get_gender_obj(self, instance):
        return self.get_data_profile_permission_r(
            basis_ser.GenderSerializer,
            basis_ser.models.GenderModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_birth_obj(self, instance):
        return self.get_data_profile_permission_r(
            basis_ser.BirthSerializer,
            basis_ser.models.BirthModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_lang_obj(self, instance):
        return self.get_data_profile_permission_r(
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
    def get_mail_obj(self, instance):
        return self.get_data_profile_permission_r(
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
    
    def get_relationship_obj(self, instance):
        return self.get_data_profile_permission_r(
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
    def get_hobby_obj(self, instance):
        return self.get_data_profile_permission_r(
            you_ser.HobbySerializer,
            you_ser.models.HobbyModel.objects.filter(profile_model=instance.id),
            instance
        )

    def get_you_obj(self, instance):
        return self.get_data_profile_permission_r(
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


class ProfileBaseSerializer(custom_field.FieldSerializer):
    name_field = 'profile_base'
    #
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    picture = SerializerMethodField()

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
        return get_profile_picture(instance.id)


class PersonalSettingSerializer(data_field.FieldSerializer):
    name_field = 'personal_settings'

    class Meta:
        model = PersonalSettingModel
        fields = '__all__'

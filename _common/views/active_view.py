
#


def change_active_instance(queryset):
    if queryset.filter(is_active=True).exists():
        instance = queryset.get(is_active=True)
        instance.is_active = False
        instance.save()

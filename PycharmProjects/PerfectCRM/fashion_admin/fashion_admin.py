from crm import models


enable_admins = {}

class Baseadmin(object):

    list_display = []
    list_filter = []
    list_editable = []
    search_fields = []
    filter_horizontal = []
    list_per_page = 1

class CustomerAdmin(Baseadmin):

    list_display = ['id', 'qq', 'source', 'status', 'date']
    list_filter = ['qq', 'source', 'status', 'date']
    # model = models.Customer

class ClassListAdmin(Baseadmin):

    list_display = ['branch','course','class_type_choices','semester']
    # model = models.Customer

class UserProfileAdmin(Baseadmin):
    list_display = ['user','name']
    list_filter = ['user','name']


def register(model_class,admin_class):
    if model_class._meta.app_label not in enable_admins:
        enable_admins[model_class._meta.app_label] = {}

    admin_class.model = model_class
    enable_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class


register(models.Customer,CustomerAdmin)
register(models.ClassList,ClassListAdmin)
register(models.UserProfile,UserProfileAdmin)

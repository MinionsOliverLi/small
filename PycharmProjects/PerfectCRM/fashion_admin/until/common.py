#__Author__:oliver
#__DATE__:1/9/17


def table_filter(request,admin_class):
    '''
    table过滤数据
    :param request:
    :param admin_class: 自定义admin类
    :return: 返回过滤后的数据
    '''
    filter_conditions = {}
    for k,v in request.GET.items():
        if v:
            filter_conditions[k] = v

    return admin_class.model.objects.filter(**filter_conditions),filter_conditions
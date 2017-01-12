from django.shortcuts import render
from fashion_admin import fashion_admin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from fashion_admin.until.common import table_filter
# Create your views here.


def index(request):

    return render(request,'fashion_admin/table_index.html',{'table_list': fashion_admin.enable_admins})


def show_table(request,app_name,table_name):

    admin_class = fashion_admin.enable_admins[app_name][table_name]
    #根据过滤条件从数据库获取数据
    obj_list,filter_conditions = table_filter(request,admin_class)
    print(obj_list,filter_conditions)

    #django内置分页，只需要把数据集和每页显示几条数据即可
    paginator = Paginator(obj_list,admin_class.list_per_page)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render(request,'fashion_admin/table.html',{'admin_class': admin_class,
                                                      'data': data,
                                                      'filter_conditions':filter_conditions})
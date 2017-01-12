# __Author__:oliver
# __DATE__:1/6/17

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def get_app_name(admin):
    return admin.model._meta.verbose_name_plural


@register.simple_tag
def build_row(obj, admin_class):
    row = ""
    for column in admin_class.list_display:
        field = obj._meta.get_field(column)
        print(field)
        if field.choices:
            column_data = getattr(obj, "get_%s_display" % column)()

        else:
            column_data = getattr(obj, column)

        if type(column_data).__name__ == 'datetime':
            column_data = column_data.strftime("%Y-%m-%d %H:%M:%S")

        row += "<td>%s</td>" % column_data
    return mark_safe(row)


@register.simple_tag
def get_page_ele(loop_counter, data):
    if abs(data.number - loop_counter) <= 1:
        ele_class = ""
        if data.number == loop_counter:
            ele_class = "active"
        ele = '<li class="%s"><a href="?page=%s">%s</a></li>' % (ele_class, loop_counter, loop_counter)

        return mark_safe(ele)
    return ''


@register.simple_tag
def render_filter_ele(condition, admin_class, filter_conditions):
    select_ele = '''<select class="form-control" name='%s' ><option value=''>----</option>''' % condition
    field_obj = admin_class.model._meta.get_field(condition)
    if field_obj.choices:
        selected = ''
        for choice_item in field_obj.choices:
            print("choice", choice_item, filter_conditions.get(condition), type(filter_conditions.get(condition)))
            if filter_conditions.get(condition) == str(choice_item[0]):
                selected = "selected"

            select_ele += '''<option value='%s' %s>%s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''

    if type(field_obj).__name__ == "ForeignKey":
        selected = ''
        for choice_item in field_obj.get_choices()[1:]:
            if filter_conditions.get(condition) == str(choice_item[0]):
                selected = "selected"
            select_ele += '''<option value='%s' %s>%s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''
    select_ele += "</select>"
    return mark_safe(select_ele)
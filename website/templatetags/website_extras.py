from django import template

register = template.Library()


@register.filter(name='modulo')
def modull_tag(number, divider):
    try:
        return int(number) % int(divider)
    except (ValueError, ZeroDivisionError):
        return None


@register.filter(name='range')
def range_tag(number):
    return range(number)


@register.filter(name='lookup')
def get_item_via_index(list_, index):
    return list_[index]

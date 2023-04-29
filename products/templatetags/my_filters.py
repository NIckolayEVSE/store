from django import template

register = template.Library()


@register.filter(name='times')
def times(value: int):
    return range(value)

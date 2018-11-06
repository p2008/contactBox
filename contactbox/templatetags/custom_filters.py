from django import template
from datetime import datetime

register = template.Library()


@register.filter
def if_yes_no(value):
    if value:
        return 'Yes'
    else:
        return 'No'


@register.filter
def count_future(value):
    current_date = datetime.now().strftime("%Y-%m-%d")
    number = value.filter(date__gte=current_date).count()

    return number

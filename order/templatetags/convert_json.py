import json
from django import template
register = template.Library()


@register.filter(name='convert_object')
def convert_object(value):
    data = json.loads(value)

    print(data)
    return data
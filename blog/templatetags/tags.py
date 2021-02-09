from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    dictionary = context['request'].GET.copy()
    for key, value in kwargs.items():
        dictionary[key] = value
    for key in [key for key, value in dictionary.items() if not value]:
        del dictionary[key]
    return dictionary.urlencode()

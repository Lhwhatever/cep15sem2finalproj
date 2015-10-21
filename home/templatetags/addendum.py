from django.template.loader_tags import register


@register.filter(name='fieldtype')
def fieldtype(obj):
    return obj.__class__.__name__
    
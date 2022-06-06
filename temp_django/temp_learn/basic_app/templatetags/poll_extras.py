form django import template

register = template.Library()

@register.filter(name= 'cut')
def cut(value,arg):
    """
    This cuts out all values of 'arg' form the string!
    """
    return value.replace(arg, '')

# register.filter('cut',cut)
